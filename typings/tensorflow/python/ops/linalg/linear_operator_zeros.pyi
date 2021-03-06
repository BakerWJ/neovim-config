from tensorflow.python.ops.linalg import linear_operator
from typing import Any, Optional

class LinearOperatorZeros(linear_operator.LinearOperator):
    def __init__(self, num_rows: Any, num_columns: Optional[Any] = ..., batch_shape: Optional[Any] = ..., dtype: Optional[Any] = ..., is_non_singular: bool = ..., is_self_adjoint: bool = ..., is_positive_definite: bool = ..., is_square: bool = ..., assert_proper_shapes: bool = ..., name: str = ...) -> None: ...
    def add_to_tensor(self, mat: Any, name: str = ...): ...
