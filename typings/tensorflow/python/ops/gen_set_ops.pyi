from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_DenseToDenseSetOperationOutput = namedtuple('DenseToDenseSetOperation', ['result_indices', 'result_values', 'result_shape'])

def dense_to_dense_set_operation(set1: Any, set2: Any, set_operation: Any, validate_indices: bool = ..., name: Optional[Any] = ...): ...

DenseToDenseSetOperation: Any

def dense_to_dense_set_operation_eager_fallback(set1: Any, set2: Any, set_operation: Any, validate_indices: Any, name: Any, ctx: Any): ...

_DenseToSparseSetOperationOutput = namedtuple('DenseToSparseSetOperation', ['result_indices', 'result_values', 'result_shape'])

def dense_to_sparse_set_operation(set1: Any, set2_indices: Any, set2_values: Any, set2_shape: Any, set_operation: Any, validate_indices: bool = ..., name: Optional[Any] = ...): ...

DenseToSparseSetOperation: Any

def dense_to_sparse_set_operation_eager_fallback(set1: Any, set2_indices: Any, set2_values: Any, set2_shape: Any, set_operation: Any, validate_indices: Any, name: Any, ctx: Any): ...
def set_size(set_indices: Any, set_values: Any, set_shape: Any, validate_indices: bool = ..., name: Optional[Any] = ...): ...

SetSize: Any

def set_size_eager_fallback(set_indices: Any, set_values: Any, set_shape: Any, validate_indices: Any, name: Any, ctx: Any): ...

_SparseToSparseSetOperationOutput = namedtuple('SparseToSparseSetOperation', ['result_indices', 'result_values', 'result_shape'])

def sparse_to_sparse_set_operation(set1_indices: Any, set1_values: Any, set1_shape: Any, set2_indices: Any, set2_values: Any, set2_shape: Any, set_operation: Any, validate_indices: bool = ..., name: Optional[Any] = ...): ...

SparseToSparseSetOperation: Any

def sparse_to_sparse_set_operation_eager_fallback(set1_indices: Any, set1_values: Any, set1_shape: Any, set2_indices: Any, set2_values: Any, set2_shape: Any, set_operation: Any, validate_indices: Any, name: Any, ctx: Any): ...
