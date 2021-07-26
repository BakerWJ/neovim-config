from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes
from tensorflow.python.ops import array_ops as array_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops_impl as linalg_ops_impl, math_ops as math_ops, random_ops as random_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class Initializer:
    def __call__(self, shape: Any, dtype: Optional[Any] = ...) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any): ...

class Zeros(Initializer):
    def __call__(self, shape: Any, dtype: Any = ...): ...

class Ones(Initializer):
    def __call__(self, shape: Any, dtype: Any = ...): ...

class Constant(Initializer):
    value: Any = ...
    def __init__(self, value: int = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Optional[Any] = ...): ...
    def get_config(self): ...

class RandomUniform(Initializer):
    minval: Any = ...
    maxval: Any = ...
    seed: Any = ...
    def __init__(self, minval: Any = ..., maxval: float = ..., seed: Optional[Any] = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Any = ...): ...
    def get_config(self): ...

class RandomNormal(Initializer):
    mean: Any = ...
    stddev: Any = ...
    seed: Any = ...
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Optional[Any] = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Any = ...): ...
    def get_config(self): ...

class TruncatedNormal(Initializer):
    mean: Any = ...
    stddev: Any = ...
    seed: Any = ...
    def __init__(self, mean: float = ..., stddev: float = ..., seed: Optional[Any] = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Any = ...): ...
    def get_config(self): ...

class VarianceScaling(Initializer):
    scale: Any = ...
    mode: Any = ...
    distribution: Any = ...
    seed: Any = ...
    def __init__(self, scale: float = ..., mode: str = ..., distribution: str = ..., seed: Optional[Any] = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Any = ...): ...
    def get_config(self): ...

class Orthogonal(Initializer):
    gain: Any = ...
    seed: Any = ...
    def __init__(self, gain: float = ..., seed: Optional[Any] = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Any = ...): ...
    def get_config(self): ...

class Identity(Initializer):
    gain: Any = ...
    def __init__(self, gain: float = ...) -> None: ...
    def __call__(self, shape: Any, dtype: Any = ...): ...
    def get_config(self): ...

class GlorotUniform(VarianceScaling):
    def __init__(self, seed: Optional[Any] = ...) -> None: ...
    def get_config(self): ...

class GlorotNormal(VarianceScaling):
    def __init__(self, seed: Optional[Any] = ...) -> None: ...
    def get_config(self): ...
zeros_initializer = Zeros
ones_initializer = Ones
constant_initializer = Constant
random_uniform_initializer = RandomUniform
random_normal_initializer = RandomNormal
truncated_normal_initializer = TruncatedNormal
variance_scaling_initializer = VarianceScaling
glorot_uniform_initializer = GlorotUniform
glorot_normal_initializer = GlorotNormal
orthogonal_initializer = Orthogonal
identity_initializer = Identity

def lecun_normal(seed: Optional[Any] = ...): ...
def lecun_uniform(seed: Optional[Any] = ...): ...
def he_normal(seed: Optional[Any] = ...): ...
def he_uniform(seed: Optional[Any] = ...): ...

class _RandomGenerator:
    seed: Any = ...
    def __init__(self, seed: Optional[Any] = ...) -> None: ...
    def random_normal(self, shape: Any, mean: float = ..., stddev: int = ..., dtype: Any = ...): ...
    def random_uniform(self, shape: Any, minval: Any, maxval: Any, dtype: Any): ...
    def truncated_normal(self, shape: Any, mean: Any, stddev: Any, dtype: Any): ...
zero = Zeros
zeros = Zeros
one = Ones
ones = Ones
constant = Constant
uniform = RandomUniform
random_uniform = RandomUniform
normal = RandomNormal
random_normal = RandomNormal
truncated_normal = TruncatedNormal
identity = Identity
orthogonal = Orthogonal
glorot_normal = GlorotNormal
glorot_uniform = GlorotUniform
