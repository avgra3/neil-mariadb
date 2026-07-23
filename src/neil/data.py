from dataclasses import dataclass, field as field_, asdict
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
    field: tuple[str, ...] = field_(default_factory=tuple)
    type: tuple[int, ...] = field_(default_factory=tuple)

    # @property
    # def type(self) -> tuple[int, ...]:
    #     return self.type_
    #
    # @type.setter
    # def type(self, value: tuple[int, ...]):
    #     self.type_ = value
    #
    # @property
    # def field(self) -> tuple[str, ...]:
    #     return self.field_
    #
    # @field.setter
    # def field(self, value: tuple[str, ...]):
    #     self.field_ = value


@dataclass(slots=True)
class NeilCursorConfig:
    buffered: bool = True

    def __str__(self) -> str:
        return f"buffered={self.buffered}"


@dataclass(slots=True, repr=True)
class NeilError:
    ErrorMessage: str
    SQLState: str | None = None
    ErrorNum: int | None = None

    def __str__(self) -> str:
        out = ""
        if self.SQLState:
            out = f"SQL State: {self.SQLState}\n" + out
        if self.ErrorNum:
            out = f"Error Num: {self.ErrorNum}\n" + out
        out += self.ErrorMessage
        return out


@dataclass(slots=True)
class NeilResult:
    sqlStatement: str
    updatedRows: int = 0
    returnedData: list[tuple[str | int]] | None = None
    metadata: NeilResultMetaData | None = None
    warningCount: int = 0
    warnings: list[NeilError] = field_(default_factory=list)
    errors: list[NeilError] = field_(default_factory=list)

    def __str__(self) -> str:
        out = f"{self.sqlStatement}\n"
        out += f"updated rows: {self.updatedRows}\n"
        if self.updatedRows:
            pass
        if self.metadata:
            out += str(self.metadata) + "\n"
        if self.warningCount > 0:
            out += f"warnings: {self.warningCount}\n"
            for warning in self.warnings:
                out += str(warning) + "\n"
        if len(self.errors) > 0:
            for err in self.errors:
                out += str(err) + "\n"
        return out


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
    # Type Conversion Parameters
    converter: dict[str, Callable[..., Any]] | None = field_(default_factory=dict)


def as_dict(obj) -> dict:
    return asdict(obj)
