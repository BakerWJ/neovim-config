from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, function as function, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_functional_ops as gen_functional_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.gen_functional_ops import remote_call as remote_call, symbolic_gradient as symbolic_gradient
from tensorflow.python.util import compat as compat, deprecation as deprecation, function_utils as function_utils, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def foldl(fn: Any, elems: Any, initializer: Optional[Any] = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Optional[Any] = ...): ...
def foldl_v2(fn: Any, elems: Any, initializer: Optional[Any] = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Optional[Any] = ...): ...
def foldr(fn: Any, elems: Any, initializer: Optional[Any] = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Optional[Any] = ...): ...
def foldr_v2(fn: Any, elems: Any, initializer: Optional[Any] = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., name: Optional[Any] = ...): ...
def scan(fn: Any, elems: Any, initializer: Optional[Any] = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., reverse: bool = ..., name: Optional[Any] = ...): ...
def scan_v2(fn: Any, elems: Any, initializer: Optional[Any] = ..., parallel_iterations: int = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., reverse: bool = ..., name: Optional[Any] = ...): ...
def If(cond: Any, inputs: Any, then_branch: Any, else_branch: Any, name: Optional[Any] = ...): ...
def Gradient(inputs: Any, f: Any, name: Optional[Any] = ...): ...
def While(input_: Any, cond: Any, body: Any, name: Optional[Any] = ..., hostmem: Optional[Any] = ...): ...
def For(start: Any, limit: Any, delta: Any, inputs: Any, body: Any, name: Optional[Any] = ..., hostmem: Optional[Any] = ..., rewrite_with_while: Optional[Any] = ...): ...
def partitioned_call(args: Any, f: Any, tout: Optional[Any] = ..., executing_eagerly: Optional[Any] = ..., config: Optional[Any] = ..., executor_type: Optional[Any] = ...): ...
