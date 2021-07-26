from tensorflow.python.ops.distributions import distribution
from typing import Any

class Laplace(distribution.Distribution):
    def __init__(self, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...

class LaplaceWithSoftplusScale(Laplace):
    def __init__(self, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
