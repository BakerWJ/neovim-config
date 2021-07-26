from tensorflow.core.framework import function_pb2 as function_pb2, op_def_pb2 as op_def_pb2
from tensorflow.python.framework import errors_impl as errors_impl, op_def_registry as op_def_registry
from typing import Any, Optional

def graph_to_function_def(graph: Any, operations: Any, inputs: Any, outputs: Any, out_names: Optional[Any] = ...): ...
