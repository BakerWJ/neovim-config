from tensorflow.python.framework import constant_op as constant_op, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn_ops as nn_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def sort(values: Any, axis: int = ..., direction: str = ..., name: Optional[Any] = ...): ...
def argsort(values: Any, axis: int = ..., direction: str = ..., stable: bool = ..., name: Optional[Any] = ...): ...
