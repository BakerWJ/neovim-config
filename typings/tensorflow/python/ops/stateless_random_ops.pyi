from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, gen_stateless_random_ops as gen_stateless_random_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def stateless_random_uniform(shape: Any, seed: Any, minval: int = ..., maxval: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_random_binomial(shape: Any, seed: Any, counts: Any, probs: Any, output_dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_random_gamma(shape: Any, seed: Any, alpha: Any, beta: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_random_poisson(shape: Any, seed: Any, lam: Any, dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_random_normal(shape: Any, seed: Any, mean: float = ..., stddev: float = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_truncated_normal(shape: Any, seed: Any, mean: float = ..., stddev: float = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_multinomial(logits: Any, num_samples: Any, seed: Any, output_dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_categorical(logits: Any, num_samples: Any, seed: Any, dtype: Any = ..., name: Optional[Any] = ...): ...
def stateless_multinomial_categorical_impl(logits: Any, num_samples: Any, dtype: Any, seed: Any): ...
