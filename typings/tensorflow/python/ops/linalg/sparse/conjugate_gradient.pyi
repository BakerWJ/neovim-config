from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def conjugate_gradient(operator: Any, rhs: Any, preconditioner: Optional[Any] = ..., x: Optional[Any] = ..., tol: float = ..., max_iter: int = ..., name: str = ...): ...
