from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops as linalg_ops, map_fn as map_fn, math_ops as math_ops, special_math_ops as special_math_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

band_part: Any
cholesky: Any
cholesky_solve: Any
det: Any
slogdet: Any
diag: Any
diag_part: Any
eigh: Any
eigvalsh: Any
einsum = special_math_ops.einsum
eye: Any
inv: Any
logm: Any
lu: Any
lstsq: Any
norm: Any
qr: Any
set_diag: Any
solve: Any
sqrtm: Any
svd: Any
tensordot: Any
trace: Any
transpose: Any
triangular_solve: Any

def logdet(matrix: Any, name: Optional[Any] = ...): ...
def adjoint(matrix: Any, name: Optional[Any] = ...): ...
def matrix_exponential(input: Any, name: Optional[Any] = ...): ...
def tridiagonal_solve(diagonals: Any, rhs: Any, diagonals_format: str = ..., transpose_rhs: bool = ..., conjugate_rhs: bool = ..., name: Optional[Any] = ..., partial_pivoting: bool = ...): ...
def tridiagonal_matmul(diagonals: Any, rhs: Any, diagonals_format: str = ..., name: Optional[Any] = ...): ...
def matrix_rank(a: Any, tol: Optional[Any] = ..., validate_args: bool = ..., name: Optional[Any] = ...): ...
def pinv(a: Any, rcond: Optional[Any] = ..., validate_args: bool = ..., name: Optional[Any] = ...): ...
def lu_solve(lower_upper: Any, perm: Any, rhs: Any, validate_args: bool = ..., name: Optional[Any] = ...): ...
def lu_matrix_inverse(lower_upper: Any, perm: Any, validate_args: bool = ..., name: Optional[Any] = ...): ...
def lu_reconstruct(lower_upper: Any, perm: Any, validate_args: bool = ..., name: Optional[Any] = ...): ...
def lu_reconstruct_assertions(lower_upper: Any, perm: Any, validate_args: Any): ...
