from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, gen_math_ops as gen_math_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def histogram_fixed_width_bins(values: Any, value_range: Any, nbins: int = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def histogram_fixed_width(values: Any, value_range: Any, nbins: int = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
