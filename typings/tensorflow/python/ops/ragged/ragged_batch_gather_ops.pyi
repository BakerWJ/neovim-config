from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_gather_ops as ragged_gather_ops, ragged_tensor as ragged_tensor, ragged_util as ragged_util
from typing import Any, Optional

def batch_gather(params: Any, indices: Any, name: Optional[Any] = ...): ...
