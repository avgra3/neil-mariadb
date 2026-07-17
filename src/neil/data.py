from dataclasses import dataclass, field


@dataclass(slots=True, repr=True)
class NeilError:
    ErrorMessage: str
    SQLState: str | None = None
    ErrorNum: int | None = None


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
