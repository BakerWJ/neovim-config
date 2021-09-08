from tensorflow.core.framework import api_def_pb2 as api_def_pb2, op_def_pb2 as op_def_pb2
from tensorflow.python.util import compat as compat, tf_contextlib as tf_contextlib
from typing import Any, Optional

class ScopedTFStatus:
    status: Any = ...
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFGraph:
    graph: Any = ...
    deleter: Any = ...
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFImportGraphDefOptions:
    options: Any = ...
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFImportGraphDefResults:
    results: Any = ...
    def __init__(self, results: Any) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFFunction:
    func: Any = ...
    deleter: Any = ...
    def __init__(self, func: Any) -> None: ...
    def __del__(self) -> None: ...

class ScopedTFBuffer:
    buffer: Any = ...
    def __init__(self, buf_string: Any) -> None: ...
    def __del__(self) -> None: ...

class ApiDefMap:
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...
    def put_api_def(self, text: Any) -> None: ...
    def get_api_def(self, op_name: Any): ...
    def get_op_def(self, op_name: Any): ...
    def op_names(self): ...

def tf_buffer(data: Optional[Any] = ...) -> None: ...
def tf_output(c_op: Any, index: Any): ...
def tf_operations(graph: Any) -> None: ...
def new_tf_operations(graph: Any) -> None: ...