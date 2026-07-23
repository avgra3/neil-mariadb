from neil.data import (
    NeilResult,
    NeilConfig,
    NeilError,
    NeilCursorConfig,
    NeilResultMetaData,
    as_dict,
)
from neil.defaults import LOGGER
from .utils import remove_after_characters, remove_between_characters
import mariadb
from datetime import datetime
import logging
from collections.abc import Callable
from typing import Any


class NeilPool:
    def __init__(
        self,
        conns: NeilConfig,
        logger: logging.Logger = LOGGER,
        pool_size: int = 3,
        cursor_conf: NeilCursorConfig | None = None,
    ):
        self.pool_size = pool_size
        self.log = logger
        self.pool_number = 1
        self.dbCons = self._extract_dbCons(dbCons=conns)
        self.pool = self._create_pool()
        self.cursor_conf = (
            cursor_conf if cursor_conf is not None else NeilCursorConfig()
        )

    def close_connection(self) -> None:
        if self.pool is None:
            return
        self.log.info("Attempting to close pool...")
        self.pool.close()
        self.log.info("Pool has been closed.")

    @staticmethod
    def _extract_dbCons(
        dbCons: NeilConfig,
    ) -> dict[str, str | int | bool | None | dict[str, Callable[..., Any]]]:
        return as_dict(obj=dbCons)

    def _create_pool(self) -> mariadb.ConnectionPool | None:
        try:
            pool = mariadb.ConnectionPool(
                pool_size=self.pool_size,
                pool_name=f"txcombo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}",
                **self.dbCons,
            )
            return pool
        except mariadb.ProgrammingError as e:
            self.log.critical(
                f"An error occured while trying to make a connection pool: {e}"
            )
        except mariadb.Error as e:
            self.log.critical(
                f"An error occured while trying to make a connection pool: {e}"
            )
        except Exception as e:
            self.log.critical(
                f"An error occured while trying to make a connection pool: {e}"
            )

    @staticmethod
    def _split_sql(sql_script: str, delim: str = ";") -> list[str]:
        return [x for x in sql_script.split(delim) if x.strip() != ""]

    @staticmethod
    def _remove_comments(
        sql_script: str,
        line_comment: str = "--",
        multiline_comment: tuple[str, str] = ("/*", "*/"),
    ) -> str:
        # Removing inline comments
        sql_script = remove_after_characters(chars=sql_script, to_remove=line_comment)
        # Removing multiline comments
        sql_script = remove_between_characters(
            string=sql_script, bounds=multiline_comment
        )
        return sql_script

    def execute_script(
        self,
        sql_script: str,
        params: list[list[Any]] | None = None,
        delim: str = ";",
        line_comment: str = "--",
        multiline_comment: tuple[str, str] = ("/*", "*/"),
    ) -> list[NeilResult]:
        results = []
        try:
            sql_script_no_comments: str = self._remove_comments(
                sql_script=sql_script,
                line_comment=line_comment,
                multiline_comment=multiline_comment,
            )
            sql_queries: list[str] = self._split_sql(
                sql_script=sql_script_no_comments, delim=delim
            )
            if len(results) > 0:
                self.log.critical(results)
            for query in sql_queries:
                if query.strip() != "":
                    results.append(self.execute_sql(sql=query, params=params))
        except Exception as e:
            self.log.critical(f"Fatal error found! {e}")
        return results

    def execute_sql(self, sql: str, params: list[Any] | None = None) -> NeilResult:
        """
        This assumes that the sql query has been cleaned
        and we can get a connection from the connection pool
        """
        result = NeilResult(sqlStatement=sql, updatedRows=0)
        if self.pool is None:
            self.log.critical("Connection to pool is none, exiting")
            return result
        try:
            with self.pool.get_connection() as conn:
                with conn.cursor(**as_dict(self.cursor_conf)) as cur:
                    _params = params if params is not None and "?" in sql else ()
                    self.log.info(f"Executing sql:\n{sql.strip()}")
                    if _params is not None and len(_params) > 0:
                        self.log.info(f"With the following parameters: {_params}")
                    cur.execute(statement=sql.strip(), data=_params)
                    if cur.description is not None:
                        result.returnedData = cur.fetchall()
                        result.updatedRows = cur.rowcount
                        self.log.info(f"Inserted/Modified rows: {result.updatedRows:,}")
                    else:
                        result.updatedRows = cur.rowcount
                        self.log.info(f"Updated rows: {result.updatedRows:,}")
                    if cur.warnings > 0:
                        result.warningCount = cur.warnings
                        result.warnings = conn.show_warnings()
                        for warn in result.warnings:
                            self.log.warning(warn)
                    if cur.metadata:
                        result.metadata = NeilResultMetaData(**cur.metadata)
                    else:
                        result.metadata = None
                conn.close()
        except mariadb.ProgrammingError as e:
            self.log.error(f"Mariadb programming error: {e}")
            result.errors.append(e)
        except mariadb.Error as e:
            self.log.error(f"Mariadb error: {e}")
            result.errors.append(e)
        except mariadb.PoolError as e:
            self.log.error(f"Pool error: {e}")
            result.errors.append(e)
        except Exception as e:
            self.log.error(f"An unknown error occured: {e}")
            result.errors.append(NeilError(ErrorMessage=repr(e)))
        return result
