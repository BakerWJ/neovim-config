from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_gather_ops as ragged_gather_ops, ragged_tensor as ragged_tensor, ragged_util as ragged_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def concat(values: Any, axis: Any, name: Optional[Any] = ...): ...
def stack(values: Any, axis: int = ..., name: Optional[Any] = ...): ...
