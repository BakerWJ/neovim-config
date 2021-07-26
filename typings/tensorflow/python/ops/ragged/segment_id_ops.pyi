from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_util as ragged_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def row_splits_to_segment_ids(splits: Any, name: Optional[Any] = ..., out_type: Optional[Any] = ...): ...
def segment_ids_to_row_splits(segment_ids: Any, num_segments: Optional[Any] = ..., out_type: Optional[Any] = ..., name: Optional[Any] = ...): ...
