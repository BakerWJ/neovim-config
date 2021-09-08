from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def batch_cholesky(input: Any, name: Optional[Any] = ...): ...

BatchCholesky: Any

def batch_cholesky_eager_fallback(input: Any, name: Any, ctx: Any): ...
def batch_cholesky_grad(l: Any, grad: Any, name: Optional[Any] = ...): ...

BatchCholeskyGrad: Any

def batch_cholesky_grad_eager_fallback(l: Any, grad: Any, name: Any, ctx: Any): ...
def batch_matrix_determinant(input: Any, name: Optional[Any] = ...): ...

BatchMatrixDeterminant: Any

def batch_matrix_determinant_eager_fallback(input: Any, name: Any, ctx: Any): ...
def batch_matrix_inverse(input: Any, adjoint: bool = ..., name: Optional[Any] = ...): ...

BatchMatrixInverse: Any

def batch_matrix_inverse_eager_fallback(input: Any, adjoint: Any, name: Any, ctx: Any): ...
def batch_matrix_solve(matrix: Any, rhs: Any, adjoint: bool = ..., name: Optional[Any] = ...): ...

BatchMatrixSolve: Any

def batch_matrix_solve_eager_fallback(matrix: Any, rhs: Any, adjoint: Any, name: Any, ctx: Any): ...
def batch_matrix_solve_ls(matrix: Any, rhs: Any, l2_regularizer: Any, fast: bool = ..., name: Optional[Any] = ...): ...

BatchMatrixSolveLs: Any

def batch_matrix_solve_ls_eager_fallback(matrix: Any, rhs: Any, l2_regularizer: Any, fast: Any, name: Any, ctx: Any): ...
def batch_matrix_triangular_solve(matrix: Any, rhs: Any, lower: bool = ..., adjoint: bool = ..., name: Optional[Any] = ...): ...

BatchMatrixTriangularSolve: Any

def batch_matrix_triangular_solve_eager_fallback(matrix: Any, rhs: Any, lower: Any, adjoint: Any, name: Any, ctx: Any): ...
def batch_self_adjoint_eig(input: Any, name: Optional[Any] = ...): ...

BatchSelfAdjointEig: Any

def batch_self_adjoint_eig_eager_fallback(input: Any, name: Any, ctx: Any): ...

_BatchSelfAdjointEigV2Output = namedtuple('BatchSelfAdjointEigV2', ['e', 'v'])

def batch_self_adjoint_eig_v2(input: Any, compute_v: bool = ..., name: Optional[Any] = ...): ...

BatchSelfAdjointEigV2: Any

def batch_self_adjoint_eig_v2_eager_fallback(input: Any, compute_v: Any, name: Any, ctx: Any): ...

_BatchSvdOutput = namedtuple('BatchSvd', ['s', 'u', 'v'])

def batch_svd(input: Any, compute_uv: bool = ..., full_matrices: bool = ..., name: Optional[Any] = ...): ...

BatchSvd: Any

def batch_svd_eager_fallback(input: Any, compute_uv: Any, full_matrices: Any, name: Any, ctx: Any): ...
def cholesky(input: Any, name: Optional[Any] = ...): ...

Cholesky: Any

def cholesky_eager_fallback(input: Any, name: Any, ctx: Any): ...
def cholesky_grad(l: Any, grad: Any, name: Optional[Any] = ...): ...

CholeskyGrad: Any

def cholesky_grad_eager_fallback(l: Any, grad: Any, name: Any, ctx: Any): ...

_EigOutput = namedtuple('Eig', ['e', 'v'])

def eig(input: Any, Tout: Any, compute_v: bool = ..., name: Optional[Any] = ...): ...

Eig: Any

def eig_eager_fallback(input: Any, Tout: Any, compute_v: Any, name: Any, ctx: Any): ...
def einsum(inputs: Any, equation: Any, name: Optional[Any] = ...): ...

Einsum: Any

def einsum_eager_fallback(inputs: Any, equation: Any, name: Any, ctx: Any): ...

_LogMatrixDeterminantOutput = namedtuple('LogMatrixDeterminant', ['sign', 'log_abs_determinant'])

def log_matrix_determinant(input: Any, name: Optional[Any] = ...): ...

LogMatrixDeterminant: Any

def log_matrix_determinant_eager_fallback(input: Any, name: Any, ctx: Any): ...

_LuOutput = namedtuple('Lu', ['lu', 'p'])

def lu(input: Any, output_idx_type: Any = ..., name: Optional[Any] = ...): ...

Lu: Any

def lu_eager_fallback(input: Any, output_idx_type: Any, name: Any, ctx: Any): ...
def matrix_determinant(input: Any, name: Optional[Any] = ...): ...

MatrixDeterminant: Any

def matrix_determinant_eager_fallback(input: Any, name: Any, ctx: Any): ...
def matrix_exponential(input: Any, name: Optional[Any] = ...): ...

MatrixExponential: Any

def matrix_exponential_eager_fallback(input: Any, name: Any, ctx: Any): ...
def matrix_inverse(input: Any, adjoint: bool = ..., name: Optional[Any] = ...): ...

MatrixInverse: Any

def matrix_inverse_eager_fallback(input: Any, adjoint: Any, name: Any, ctx: Any): ...
def matrix_logarithm(input: Any, name: Optional[Any] = ...): ...

MatrixLogarithm: Any

def matrix_logarithm_eager_fallback(input: Any, name: Any, ctx: Any): ...
def matrix_solve(matrix: Any, rhs: Any, adjoint: bool = ..., name: Optional[Any] = ...): ...

MatrixSolve: Any

def matrix_solve_eager_fallback(matrix: Any, rhs: Any, adjoint: Any, name: Any, ctx: Any): ...
def matrix_solve_ls(matrix: Any, rhs: Any, l2_regularizer: Any, fast: bool = ..., name: Optional[Any] = ...): ...

MatrixSolveLs: Any

def matrix_solve_ls_eager_fallback(matrix: Any, rhs: Any, l2_regularizer: Any, fast: Any, name: Any, ctx: Any): ...
def matrix_square_root(input: Any, name: Optional[Any] = ...): ...

MatrixSquareRoot: Any

def matrix_square_root_eager_fallback(input: Any, name: Any, ctx: Any): ...
def matrix_triangular_solve(matrix: Any, rhs: Any, lower: bool = ..., adjoint: bool = ..., name: Optional[Any] = ...): ...

MatrixTriangularSolve: Any

def matrix_triangular_solve_eager_fallback(matrix: Any, rhs: Any, lower: Any, adjoint: Any, name: Any, ctx: Any): ...

_QrOutput = namedtuple('Qr', ['q', 'r'])

def qr(input: Any, full_matrices: bool = ..., name: Optional[Any] = ...): ...

Qr: Any

def qr_eager_fallback(input: Any, full_matrices: Any, name: Any, ctx: Any): ...
def self_adjoint_eig(input: Any, name: Optional[Any] = ...): ...

SelfAdjointEig: Any

def self_adjoint_eig_eager_fallback(input: Any, name: Any, ctx: Any): ...

_SelfAdjointEigV2Output = namedtuple('SelfAdjointEigV2', ['e', 'v'])

def self_adjoint_eig_v2(input: Any, compute_v: bool = ..., name: Optional[Any] = ...): ...

SelfAdjointEigV2: Any

def self_adjoint_eig_v2_eager_fallback(input: Any, compute_v: Any, name: Any, ctx: Any): ...

_SvdOutput = namedtuple('Svd', ['s', 'u', 'v'])

def svd(input: Any, compute_uv: bool = ..., full_matrices: bool = ..., name: Optional[Any] = ...): ...

Svd: Any

def svd_eager_fallback(input: Any, compute_uv: Any, full_matrices: Any, name: Any, ctx: Any): ...
def tridiagonal_mat_mul(superdiag: Any, maindiag: Any, subdiag: Any, rhs: Any, name: Optional[Any] = ...): ...

TridiagonalMatMul: Any

def tridiagonal_mat_mul_eager_fallback(superdiag: Any, maindiag: Any, subdiag: Any, rhs: Any, name: Any, ctx: Any): ...
def tridiagonal_solve(diagonals: Any, rhs: Any, partial_pivoting: bool = ..., name: Optional[Any] = ...): ...

TridiagonalSolve: Any

def tridiagonal_solve_eager_fallback(diagonals: Any, rhs: Any, partial_pivoting: Any, name: Any, ctx: Any): ...