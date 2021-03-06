from tensorflow.python.ops.gen_random_ops import *
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, random_seed as random_seed, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_random_ops as gen_random_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def random_normal(shape: Any, mean: float = ..., stddev: float = ..., dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def parameterized_truncated_normal(shape: Any, means: float = ..., stddevs: float = ..., minvals: Any = ..., maxvals: float = ..., dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def truncated_normal(shape: Any, mean: float = ..., stddev: float = ..., dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def random_uniform(shape: Any, minval: int = ..., maxval: Optional[Any] = ..., dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def random_shuffle(value: Any, seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def random_crop(value: Any, size: Any, seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def multinomial(logits: Any, num_samples: Any, seed: Optional[Any] = ..., name: Optional[Any] = ..., output_dtype: Optional[Any] = ...): ...
def categorical(logits: Any, num_samples: Any, dtype: Optional[Any] = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def multinomial_categorical_impl(logits: Any, num_samples: Any, dtype: Any, seed: Any): ...
def random_gamma(shape: Any, alpha: Any, beta: Optional[Any] = ..., dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def random_poisson(lam: Any, shape: Any, dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def random_poisson_v2(shape: Any, lam: Any, dtype: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
