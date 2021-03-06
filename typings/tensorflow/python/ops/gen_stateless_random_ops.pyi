from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def stateless_multinomial(logits: Any, num_samples: Any, seed: Any, output_dtype: Any = ..., name: Optional[Any] = ...): ...

StatelessMultinomial: Any

def stateless_multinomial_eager_fallback(logits: Any, num_samples: Any, seed: Any, output_dtype: Any, name: Any, ctx: Any): ...
def stateless_random_binomial(shape: Any, seed: Any, counts: Any, probs: Any, dtype: Any = ..., name: Optional[Any] = ...): ...

StatelessRandomBinomial: Any

def stateless_random_binomial_eager_fallback(shape: Any, seed: Any, counts: Any, probs: Any, dtype: Any, name: Any, ctx: Any): ...
def stateless_random_gamma_v2(shape: Any, seed: Any, alpha: Any, name: Optional[Any] = ...): ...

StatelessRandomGammaV2: Any

def stateless_random_gamma_v2_eager_fallback(shape: Any, seed: Any, alpha: Any, name: Any, ctx: Any): ...
def stateless_random_normal(shape: Any, seed: Any, dtype: Any = ..., name: Optional[Any] = ...): ...

StatelessRandomNormal: Any

def stateless_random_normal_eager_fallback(shape: Any, seed: Any, dtype: Any, name: Any, ctx: Any): ...
def stateless_random_poisson(shape: Any, seed: Any, lam: Any, dtype: Any, name: Optional[Any] = ...): ...

StatelessRandomPoisson: Any

def stateless_random_poisson_eager_fallback(shape: Any, seed: Any, lam: Any, dtype: Any, name: Any, ctx: Any): ...
def stateless_random_uniform(shape: Any, seed: Any, dtype: Any = ..., name: Optional[Any] = ...): ...

StatelessRandomUniform: Any

def stateless_random_uniform_eager_fallback(shape: Any, seed: Any, dtype: Any, name: Any, ctx: Any): ...
def stateless_random_uniform_full_int(shape: Any, seed: Any, dtype: Any = ..., name: Optional[Any] = ...): ...

StatelessRandomUniformFullInt: Any

def stateless_random_uniform_full_int_eager_fallback(shape: Any, seed: Any, dtype: Any, name: Any, ctx: Any): ...
def stateless_random_uniform_int(shape: Any, seed: Any, minval: Any, maxval: Any, name: Optional[Any] = ...): ...

StatelessRandomUniformInt: Any

def stateless_random_uniform_int_eager_fallback(shape: Any, seed: Any, minval: Any, maxval: Any, name: Any, ctx: Any): ...
def stateless_truncated_normal(shape: Any, seed: Any, dtype: Any = ..., name: Optional[Any] = ...): ...

StatelessTruncatedNormal: Any

def stateless_truncated_normal_eager_fallback(shape: Any, seed: Any, dtype: Any, name: Any, ctx: Any): ...
