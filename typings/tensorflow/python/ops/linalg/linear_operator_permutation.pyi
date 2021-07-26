from tensorflow.python.ops.linalg import linear_operator
from typing import Any, Optional

class LinearOperatorPermutation(linear_operator.LinearOperator):
    def __init__(self, perm: Any, dtype: Any = ..., is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: Optional[Any] = ..., name: str = ...) -> None: ...
    @property
    def perm(self): ...
