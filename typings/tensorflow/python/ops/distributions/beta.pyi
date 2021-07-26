from tensorflow.python.ops.distributions import distribution
from typing import Any, Optional

class Beta(distribution.Distribution):
    def __init__(self, concentration1: Optional[Any] = ..., concentration0: Optional[Any] = ..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def concentration1(self): ...
    @property
    def concentration0(self): ...
    @property
    def total_concentration(self): ...

class BetaWithSoftplusConcentration(Beta):
    def __init__(self, concentration1: Any, concentration0: Any, validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
