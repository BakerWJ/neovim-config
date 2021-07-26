from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gradients as gradients, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def compute_gradient(x: Any, x_shape: Any, y: Any, y_shape: Any, x_init_value: Optional[Any] = ..., delta: float = ..., init_targets: Optional[Any] = ..., extra_feed_dict: Optional[Any] = ...): ...
def compute_gradient_error(x: Any, x_shape: Any, y: Any, y_shape: Any, x_init_value: Optional[Any] = ..., delta: float = ..., init_targets: Optional[Any] = ..., extra_feed_dict: Optional[Any] = ...): ...
