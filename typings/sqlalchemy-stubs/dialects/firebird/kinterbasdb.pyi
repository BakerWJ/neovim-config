from typing import Any
from typing import Optional

from .base import FBDialect as FBDialect
from .base import FBExecutionContext as FBExecutionContext
from ... import types as sqltypes
from ... import util as util

class _kinterbasdb_numeric:
    def bind_processor(self, dialect: Any): ...

class _FBNumeric_kinterbasdb(_kinterbasdb_numeric, sqltypes.Numeric): ...
class _FBFloat_kinterbasdb(_kinterbasdb_numeric, sqltypes.Float): ...

class FBExecutionContext_kinterbasdb(FBExecutionContext):
    @property
    def rowcount(self): ...

class FBDialect_kinterbasdb(FBDialect):
    driver: str = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    execution_ctx_cls: Any = ...
    supports_native_decimal: bool = ...
    colspecs: Any = ...
    enable_rowcount: Any = ...
    type_conv: Any = ...
    concurrency_level: Any = ...
    retaining: Any = ...
    def __init__(
        self,
        type_conv: int = ...,
        concurrency_level: int = ...,
        enable_rowcount: bool = ...,
        retaining: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def do_execute(
        self,
        cursor: Any,
        statement: Any,
        parameters: Any,
        context: Optional[Any] = ...,
    ) -> None: ...
    def do_rollback(self, dbapi_connection: Any) -> None: ...
    def do_commit(self, dbapi_connection: Any) -> None: ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...

dialect = FBDialect_kinterbasdb