from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, sort_ops as sort_ops
from tensorflow.python.ops.ragged import ragged_functional_ops as ragged_functional_ops, ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor, ragged_util as ragged_util, segment_id_ops as segment_id_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def boolean_mask(data: Any, mask: Any, name: Optional[Any] = ...): ...
def tile(input: Any, multiples: Any, name: Optional[Any] = ...): ...
def expand_dims(input: Any, axis: Any, name: Optional[Any] = ...): ...
def size(input: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def rank(input: Any, name: Optional[Any] = ...): ...
def ragged_one_hot(indices: Any, depth: Any, on_value: Optional[Any] = ..., off_value: Optional[Any] = ..., axis: Optional[Any] = ..., dtype: Optional[Any] = ..., name: Optional[Any] = ...): ...
def stack_dynamic_partitions(data: Any, partitions: Any, num_partitions: Any, name: Optional[Any] = ...): ...
def reverse(tensor: Any, axis: Any, name: Optional[Any] = ...): ...
