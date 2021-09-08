from typing import Any

from .enumerated import ENUM as ENUM
from .enumerated import SET as SET
from .types import DATETIME as DATETIME
from .types import TIME as TIME
from .types import TIMESTAMP as TIMESTAMP
from ... import log as log
from ... import util as util

class ReflectedState:
    columns: Any = ...
    table_options: Any = ...
    table_name: Any = ...
    keys: Any = ...
    fk_constraints: Any = ...
    ck_constraints: Any = ...
    def __init__(self) -> None: ...

class MySQLTableDefinitionParser:
    dialect: Any = ...
    preparer: Any = ...
    def __init__(self, dialect: Any, preparer: Any) -> None: ...
    def parse(self, show_create: Any, charset: Any): ...