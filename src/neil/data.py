from dataclasses import dataclass, field


@dataclass(slots=True)
class NeilError:
    ErrorMessage: str
    SQLState: str | None = None
    ErrorNum: int | None = None

    def __repr__(self) -> str:
        sql_state = self.SQLState if self.SQLState is not None else "n/a"
        sql_err_num = self.ErrorNum if self.ErrorNum is not None else "n/a"
        return f"SQL State: {sql_state} \tSQL Error Number: {sql_err_num}\n{self.ErrorMessage}"


@dataclass(slots=True)
class NeilResult:
    sqlStatement: str
    updatedRows: int = 0
    returnedData: list[tuple[str | int]] | None = None
    metadata: dict[str, str | int] = field(default_factory=dict)
    warningCount: int = 0
    warnings: list[NeilError] = field(default_factory=list)
    errors: list[NeilError] = field(default_factory=list)


@dataclass(slots=True)
class NeilConfig:
    username: str
    password: str
    database: str = ""
    hostname: str = "localhost"
    port: int = 3306

    def as_dict(self) -> dict[str, str | int | bool]:
        return {
            "user": self.username,
            "password": self.password,
            "host": self.hostname,
            "port": self.port,
            "database": self.database,
        }
