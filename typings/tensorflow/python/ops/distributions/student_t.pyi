from tensorflow.python.ops.distributions import distribution
from typing import Any

class StudentT(distribution.Distribution):
    def __init__(self, df: Any, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def df(self): ...
    @property
    def loc(self): ...
    @property
    def scale(self): ...

class StudentTWithAbsDfSoftplusScale(StudentT):
    def __init__(self, df: Any, loc: Any, scale: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
