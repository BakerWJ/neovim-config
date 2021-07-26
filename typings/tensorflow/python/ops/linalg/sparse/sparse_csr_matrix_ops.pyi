from tensorflow.python.ops.linalg.sparse.gen_sparse_csr_matrix_ops import *
import abc
import collections as collections
from typing import Any, Optional

class DenseShapeAndType: ...

def dense_shape_and_type(matrix: Any): ...
def matmul(a: Any, b: Any, transpose_a: bool = ..., transpose_b: bool = ..., adjoint_a: bool = ..., adjoint_b: bool = ..., name: Optional[Any] = ...): ...

class SparseMatrix(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self) -> Any: ...
    @abc.abstractmethod
    def to_dense(self) -> Any: ...
    @abc.abstractmethod
    def to_sparse_tensor(self) -> Any: ...
    @property
    def graph(self): ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    @property
    def eager_handle_data(self): ...
    def conj(self): ...
    def hermitian_transpose(self): ...
    def nnz(self): ...
    nonzero: Any = ...
    def sorted_indices(self): ...
    def transpose(self): ...

class CSRSparseMatrix(SparseMatrix):
    def __init__(self, value: Any, indices: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def to_dense(self): ...
    def to_sparse_tensor(self): ...

# Names in __all__ with no definition:
#   CSRSparseMatrixComponents
#   CSRSparseMatrixToDense
#   CSRSparseMatrixToSparseTensor
#   DenseToCSRSparseMatrix
#   SparseMatrixAdd
#   SparseMatrixMatMul
#   SparseMatrixMul
#   SparseMatrixNNZ
#   SparseMatrixOrderingAMD
#   SparseMatrixSoftmax
#   SparseMatrixSoftmaxGrad
#   SparseMatrixSparseCholesky
#   SparseMatrixSparseMatMul
#   SparseMatrixTranspose
#   SparseMatrixZeros
#   SparseTensorToCSRSparseMatrix
#   csr_sparse_matrix_components
#   csr_sparse_matrix_components_eager_fallback
#   csr_sparse_matrix_to_dense
#   csr_sparse_matrix_to_dense_eager_fallback
#   csr_sparse_matrix_to_sparse_tensor
#   csr_sparse_matrix_to_sparse_tensor_eager_fallback
#   dense_to_csr_sparse_matrix
#   dense_to_csr_sparse_matrix_eager_fallback
#   deprecated_endpoints
#   pywrap_tfe
#   sparse_matrix_add
#   sparse_matrix_add_eager_fallback
#   sparse_matrix_mat_mul
#   sparse_matrix_mat_mul_eager_fallback
#   sparse_matrix_mul
#   sparse_matrix_mul_eager_fallback
#   sparse_matrix_nnz
#   sparse_matrix_nnz_eager_fallback
#   sparse_matrix_ordering_amd
#   sparse_matrix_ordering_amd_eager_fallback
#   sparse_matrix_softmax
#   sparse_matrix_softmax_eager_fallback
#   sparse_matrix_softmax_grad
#   sparse_matrix_softmax_grad_eager_fallback
#   sparse_matrix_sparse_cholesky
#   sparse_matrix_sparse_cholesky_eager_fallback
#   sparse_matrix_sparse_mat_mul
#   sparse_matrix_sparse_mat_mul_eager_fallback
#   sparse_matrix_transpose
#   sparse_matrix_transpose_eager_fallback
#   sparse_matrix_zeros
#   sparse_matrix_zeros_eager_fallback
#   sparse_tensor_to_csr_sparse_matrix
#   sparse_tensor_to_csr_sparse_matrix_eager_fallback
#   tf_export
