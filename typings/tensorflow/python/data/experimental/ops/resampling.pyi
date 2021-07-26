from tensorflow.python.data.experimental.ops import interleave_ops as interleave_ops, scan_ops as scan_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, logging_ops as logging_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def rejection_resample(class_func: Any, target_dist: Any, initial_dist: Optional[Any] = ..., seed: Optional[Any] = ...): ...
