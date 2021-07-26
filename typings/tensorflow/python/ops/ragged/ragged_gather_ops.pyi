from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_ragged_array_ops as gen_ragged_array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor
from typing import Any, Optional

def gather(params: Any, indices: Any, validate_indices: Optional[Any] = ..., axis: int = ..., batch_dims: int = ..., name: Optional[Any] = ...): ...
def gather_nd(params: Any, indices: Any, batch_dims: int = ..., name: Optional[Any] = ...): ...
