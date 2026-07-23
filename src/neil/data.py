from dataclasses import dataclass, field, asdict
from collections.abc import Callable
from typing import Any


@dataclass(slots=True)
class NeilResultMetaData:
    catalog: tuple[str, ...]
    schema: tuple[str, ...]
    org_field: tuple[str, ...]
    table: tuple[str, ...]
    charset: tuple[int, ...]
    length: tuple[int, ...]
    max_length: tuple[int, ...]
    decimals: tuple[int, ...]
    flags: tuple[int, ...]
    ext_type_or_format: tuple[int, ...]
    field_: tuple[str, ...] = field(default_factory=tuple)
    type_: tuple[int, ...] = field(default_factory=tuple)

    @property
    def type(self) -> tuple[int, ...]:
        return self.type_

    @type.setter
    def type(self, value: tuple[int, ...]):
        self.type_ = value

    @property
    def field(self) -> tuple[str, ...]:
        return self.field_

    @field.setter
    def field(self, value: tuple[str, ...]):
        self.field_ = value


@dataclass(slots=True)
class NeilCursorConfig:
    binary: bool
    buffered: bool = True


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
    metadata: NeilResultMetaData | None = None
    warningCount: int = 0
    warnings: list[NeilError] = field(default_factory=list)
    errors: list[NeilError] = field(default_factory=list)


@dataclass(slots=True)
class NeilConfig:
    user: str
    password: str
    database: str = ""
    host: str = "localhost"
    port: int = 3306
    # Connection behaviors
    autocommit: bool = False
    compress: bool = False
    local_infile: bool = False
    init_command: str | None = None
    # Protocol and Performance Params
    binary: bool = False
    max_allowed_packet: int = 16777216  # 16MB
    cache_prep_stmts: bool = False
    prep_stmt_cache_size: int = 100
    pipeline: bool = True
    client_flag: int = 0
    # Type Conversion Parameters
    converter: dict[str, Callable[..., Any]] | None = field(default_factory=dict)


def as_dict(obj) -> dict:
    return asdict(obj)
