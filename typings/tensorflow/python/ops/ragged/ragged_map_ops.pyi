from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.ragged import ragged_config as ragged_config, ragged_tensor as ragged_tensor
from tensorflow.python.util import nest as nest
from typing import Any, Optional

def map_fn(fn: Any, elems: Any, dtype: Optional[Any] = ..., parallel_iterations: Optional[Any] = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., name: Optional[Any] = ...): ...

class _RaggedTensorComponents: ...
