from tensorflow.python.ops.distributions import gamma
from typing import Any

class Exponential(gamma.Gamma):
    def __init__(self, rate: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def rate(self): ...

class ExponentialWithSoftplusRate(Exponential):
    def __init__(self, rate: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
