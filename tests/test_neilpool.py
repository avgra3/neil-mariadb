from neil import NeilPool, as_dict
from .constants import (
    BASIC_CONFIG,
    SAMPLE_SQL_ONE,
    SAMPLE_SQL_TWO,
    SAMPLE_MULTIPLE_SQL,
    SAMPLE_SQL_WITH_LINE_COMMENTS,
    SAMPLE_SQL_WITH_MULTILINE_COMMENTS,
    SAMPLE_SQL_WITHOUT_LINE_COMMENTS,
    SAMPLE_SQL_WITHOUT_MULTILINE_COMMENTS,
)


def test_extract_db_config_correct():
    assert as_dict(obj=BASIC_CONFIG) == NeilPool._extract_dbCons(dbCons=BASIC_CONFIG)


def test_sql_split_works_as_expected():
    split_sql: list[str] = NeilPool._split_sql(sql_script=SAMPLE_MULTIPLE_SQL)
    expected: list[str] = [SAMPLE_SQL_ONE[:-1], SAMPLE_SQL_TWO[:-1]]
    assert split_sql == expected


def test_sql_remove_line_comments_mid_query():
    assert (
        NeilPool._remove_comments(sql_script=SAMPLE_SQL_WITH_LINE_COMMENTS)
        == SAMPLE_SQL_WITHOUT_LINE_COMMENTS
    )


def test_sql_remove_multiline_comments_mid_query():
    assert (
        NeilPool._remove_comments(sql_script=SAMPLE_SQL_WITH_MULTILINE_COMMENTS)
        == SAMPLE_SQL_WITHOUT_MULTILINE_COMMENTS
    )
