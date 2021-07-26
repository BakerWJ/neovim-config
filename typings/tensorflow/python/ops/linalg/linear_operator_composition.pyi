from tensorflow.python.ops.linalg import linear_operator
from typing import Any, Optional

class LinearOperatorComposition(linear_operator.LinearOperator):
    def __init__(self, operators: Any, is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def operators(self): ...
