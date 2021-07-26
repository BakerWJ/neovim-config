from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def multinomial(logits: Any, num_samples: Any, seed: int = ..., seed2: int = ..., output_dtype: Any = ..., name: Optional[Any] = ...): ...

Multinomial: Any

def multinomial_eager_fallback(logits: Any, num_samples: Any, seed: Any, seed2: Any, output_dtype: Any, name: Any, ctx: Any): ...
def parameterized_truncated_normal(shape: Any, means: Any, stdevs: Any, minvals: Any, maxvals: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

ParameterizedTruncatedNormal: Any

def parameterized_truncated_normal_eager_fallback(shape: Any, means: Any, stdevs: Any, minvals: Any, maxvals: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def random_gamma(shape: Any, alpha: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomGamma: Any

def random_gamma_eager_fallback(shape: Any, alpha: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def random_gamma_grad(alpha: Any, sample: Any, name: Optional[Any] = ...): ...

RandomGammaGrad: Any

def random_gamma_grad_eager_fallback(alpha: Any, sample: Any, name: Any, ctx: Any): ...
def random_poisson(shape: Any, rate: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomPoisson: Any

def random_poisson_eager_fallback(shape: Any, rate: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def random_poisson_v2(shape: Any, rate: Any, seed: int = ..., seed2: int = ..., dtype: Any = ..., name: Optional[Any] = ...): ...

RandomPoissonV2: Any

def random_poisson_v2_eager_fallback(shape: Any, rate: Any, seed: Any, seed2: Any, dtype: Any, name: Any, ctx: Any): ...
def random_shuffle(value: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomShuffle: Any

def random_shuffle_eager_fallback(value: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def random_standard_normal(shape: Any, dtype: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomStandardNormal: Any

def random_standard_normal_eager_fallback(shape: Any, dtype: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def random_uniform(shape: Any, dtype: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomUniform: Any

def random_uniform_eager_fallback(shape: Any, dtype: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def random_uniform_int(shape: Any, minval: Any, maxval: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

RandomUniformInt: Any

def random_uniform_int_eager_fallback(shape: Any, minval: Any, maxval: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def truncated_normal(shape: Any, dtype: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

TruncatedNormal: Any

def truncated_normal_eager_fallback(shape: Any, dtype: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
