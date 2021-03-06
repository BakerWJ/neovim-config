from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class Uniform(distribution.Distribution):
    def __init__(self, low: float = ..., high: float = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def low(self): ...
    @property
    def high(self): ...
    def range(self, name: str = ...): ...
