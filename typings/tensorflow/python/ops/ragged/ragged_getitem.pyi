from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_gather_ops as ragged_gather_ops, ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor
from typing import Any

def ragged_tensor_getitem(self, key: Any): ...
