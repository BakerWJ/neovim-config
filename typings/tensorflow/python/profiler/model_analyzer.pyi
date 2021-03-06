from tensorflow.core.profiler import tfprof_options_pb2 as tfprof_options_pb2, tfprof_output_pb2 as tfprof_output_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.profiler import option_builder as option_builder, tfprof_logger as tfprof_logger
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

ALL_ADVICE: Any

class Profiler:
    def __init__(self, graph: Optional[Any] = ..., op_log: Optional[Any] = ...) -> None: ...
    def __del__(self) -> None: ...
    def add_step(self, step: Any, run_meta: Any) -> None: ...
    def profile_python(self, options: Any): ...
    def profile_operations(self, options: Any): ...
    def profile_name_scope(self, options: Any): ...
    def profile_graph(self, options: Any): ...
    def advise(self, options: Any): ...
    def serialize_to_string(self): ...

def profile(graph: Optional[Any] = ..., run_meta: Optional[Any] = ..., op_log: Optional[Any] = ..., cmd: str = ..., options: Any = ...): ...
def advise(graph: Optional[Any] = ..., run_meta: Optional[Any] = ..., options: Any = ...): ...
