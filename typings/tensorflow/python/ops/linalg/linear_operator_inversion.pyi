from tensorflow.python.framework import ops as ops
from tensorflow.python.ops.linalg import linear_operator as linear_operator, linear_operator_util as linear_operator_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class LinearOperatorInversion(linear_operator.LinearOperator):
    def __init__(self, operator: Any, is_non_singular: Optional[Any] = ..., is_self_adjoint: Optional[Any] = ..., is_positive_definite: Optional[Any] = ..., is_square: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def operator(self): ...
