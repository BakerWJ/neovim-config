from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.module import module as module
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, linalg_ops as linalg_ops, math_ops as math_ops
from typing import Any, Optional

def convert_nonref_to_tensor(value: Any, dtype: Optional[Any] = ..., dtype_hint: Optional[Any] = ..., name: Optional[Any] = ...): ...
def base_dtype(dtype: Any): ...
def dtype_name(dtype: Any): ...
def is_ref(x: Any): ...
def assert_not_ref_type(x: Any, arg_name: Any) -> None: ...
def assert_no_entries_with_modulus_zero(x: Any, message: Optional[Any] = ..., name: str = ...): ...
def assert_zero_imag_part(x: Any, message: Optional[Any] = ..., name: str = ...): ...
def assert_compatible_matrix_dimensions(operator: Any, x: Any): ...
def assert_is_batch_matrix(tensor: Any) -> None: ...
def shape_tensor(shape: Any, name: Optional[Any] = ...): ...
def broadcast_matrix_batch_dims(batch_matrices: Any, name: Optional[Any] = ...): ...
def matrix_solve_with_broadcast(matrix: Any, rhs: Any, adjoint: bool = ..., name: Optional[Any] = ...): ...
def use_operator_or_provided_hint_unless_contradicting(operator: Any, hint_attr_name: Any, provided_hint_value: Any, message: Any): ...