from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def add_many_sparse_to_tensors_map(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

AddManySparseToTensorsMap: Any

def add_many_sparse_to_tensors_map_eager_fallback(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, container: Any, shared_name: Any, name: Any, ctx: Any): ...
def add_sparse_to_tensors_map(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

AddSparseToTensorsMap: Any

def add_sparse_to_tensors_map_eager_fallback(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, container: Any, shared_name: Any, name: Any, ctx: Any): ...

_DeserializeManySparseOutput = namedtuple('DeserializeManySparse', ['sparse_indices', 'sparse_values', 'sparse_shape'])

def deserialize_many_sparse(serialized_sparse: Any, dtype: Any, name: Optional[Any] = ...): ...

DeserializeManySparse: Any

def deserialize_many_sparse_eager_fallback(serialized_sparse: Any, dtype: Any, name: Any, ctx: Any): ...

_DeserializeSparseOutput = namedtuple('DeserializeSparse', ['sparse_indices', 'sparse_values', 'sparse_shape'])

def deserialize_sparse(serialized_sparse: Any, dtype: Any, name: Optional[Any] = ...): ...

DeserializeSparse: Any

def deserialize_sparse_eager_fallback(serialized_sparse: Any, dtype: Any, name: Any, ctx: Any): ...
def serialize_many_sparse(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, out_type: Any = ..., name: Optional[Any] = ...): ...

SerializeManySparse: Any

def serialize_many_sparse_eager_fallback(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, out_type: Any, name: Any, ctx: Any): ...
def serialize_sparse(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, out_type: Any = ..., name: Optional[Any] = ...): ...

SerializeSparse: Any

def serialize_sparse_eager_fallback(sparse_indices: Any, sparse_values: Any, sparse_shape: Any, out_type: Any, name: Any, ctx: Any): ...

_SparseAddOutput = namedtuple('SparseAdd', ['sum_indices', 'sum_values', 'sum_shape'])

def sparse_add(a_indices: Any, a_values: Any, a_shape: Any, b_indices: Any, b_values: Any, b_shape: Any, thresh: Any, name: Optional[Any] = ...): ...

SparseAdd: Any

def sparse_add_eager_fallback(a_indices: Any, a_values: Any, a_shape: Any, b_indices: Any, b_values: Any, b_shape: Any, thresh: Any, name: Any, ctx: Any): ...

_SparseAddGradOutput = namedtuple('SparseAddGrad', ['a_val_grad', 'b_val_grad'])

def sparse_add_grad(backprop_val_grad: Any, a_indices: Any, b_indices: Any, sum_indices: Any, name: Optional[Any] = ...): ...

SparseAddGrad: Any

def sparse_add_grad_eager_fallback(backprop_val_grad: Any, a_indices: Any, b_indices: Any, sum_indices: Any, name: Any, ctx: Any): ...

_SparseConcatOutput = namedtuple('SparseConcat', ['output_indices', 'output_values', 'output_shape'])

def sparse_concat(indices: Any, values: Any, shapes: Any, concat_dim: Any, name: Optional[Any] = ...): ...

SparseConcat: Any

def sparse_concat_eager_fallback(indices: Any, values: Any, shapes: Any, concat_dim: Any, name: Any, ctx: Any): ...

_SparseCrossOutput = namedtuple('SparseCross', ['output_indices', 'output_values', 'output_shape'])

def sparse_cross(indices: Any, values: Any, shapes: Any, dense_inputs: Any, hashed_output: Any, num_buckets: Any, hash_key: Any, out_type: Any, internal_type: Any, name: Optional[Any] = ...): ...

SparseCross: Any

def sparse_cross_eager_fallback(indices: Any, values: Any, shapes: Any, dense_inputs: Any, hashed_output: Any, num_buckets: Any, hash_key: Any, out_type: Any, internal_type: Any, name: Any, ctx: Any): ...
def sparse_dense_cwise_add(sp_indices: Any, sp_values: Any, sp_shape: Any, dense: Any, name: Optional[Any] = ...): ...

SparseDenseCwiseAdd: Any

def sparse_dense_cwise_add_eager_fallback(sp_indices: Any, sp_values: Any, sp_shape: Any, dense: Any, name: Any, ctx: Any): ...
def sparse_dense_cwise_div(sp_indices: Any, sp_values: Any, sp_shape: Any, dense: Any, name: Optional[Any] = ...): ...

SparseDenseCwiseDiv: Any

def sparse_dense_cwise_div_eager_fallback(sp_indices: Any, sp_values: Any, sp_shape: Any, dense: Any, name: Any, ctx: Any): ...
def sparse_dense_cwise_mul(sp_indices: Any, sp_values: Any, sp_shape: Any, dense: Any, name: Optional[Any] = ...): ...

SparseDenseCwiseMul: Any

def sparse_dense_cwise_mul_eager_fallback(sp_indices: Any, sp_values: Any, sp_shape: Any, dense: Any, name: Any, ctx: Any): ...

_SparseFillEmptyRowsOutput = namedtuple('SparseFillEmptyRows', ['output_indices', 'output_values', 'empty_row_indicator', 'reverse_index_map'])

def sparse_fill_empty_rows(indices: Any, values: Any, dense_shape: Any, default_value: Any, name: Optional[Any] = ...): ...

SparseFillEmptyRows: Any

def sparse_fill_empty_rows_eager_fallback(indices: Any, values: Any, dense_shape: Any, default_value: Any, name: Any, ctx: Any): ...

_SparseFillEmptyRowsGradOutput = namedtuple('SparseFillEmptyRowsGrad', ['d_values', 'd_default_value'])

def sparse_fill_empty_rows_grad(reverse_index_map: Any, grad_values: Any, name: Optional[Any] = ...): ...

SparseFillEmptyRowsGrad: Any

def sparse_fill_empty_rows_grad_eager_fallback(reverse_index_map: Any, grad_values: Any, name: Any, ctx: Any): ...
def sparse_reduce_max(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: bool = ..., name: Optional[Any] = ...): ...

SparseReduceMax: Any

def sparse_reduce_max_eager_fallback(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: Any, name: Any, ctx: Any): ...

_SparseReduceMaxSparseOutput = namedtuple('SparseReduceMaxSparse', ['output_indices', 'output_values', 'output_shape'])

def sparse_reduce_max_sparse(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: bool = ..., name: Optional[Any] = ...): ...

SparseReduceMaxSparse: Any

def sparse_reduce_max_sparse_eager_fallback(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: Any, name: Any, ctx: Any): ...
def sparse_reduce_sum(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: bool = ..., name: Optional[Any] = ...): ...

SparseReduceSum: Any

def sparse_reduce_sum_eager_fallback(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: Any, name: Any, ctx: Any): ...

_SparseReduceSumSparseOutput = namedtuple('SparseReduceSumSparse', ['output_indices', 'output_values', 'output_shape'])

def sparse_reduce_sum_sparse(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: bool = ..., name: Optional[Any] = ...): ...

SparseReduceSumSparse: Any

def sparse_reduce_sum_sparse_eager_fallback(input_indices: Any, input_values: Any, input_shape: Any, reduction_axes: Any, keep_dims: Any, name: Any, ctx: Any): ...

_SparseReorderOutput = namedtuple('SparseReorder', ['output_indices', 'output_values'])

def sparse_reorder(input_indices: Any, input_values: Any, input_shape: Any, name: Optional[Any] = ...): ...

SparseReorder: Any

def sparse_reorder_eager_fallback(input_indices: Any, input_values: Any, input_shape: Any, name: Any, ctx: Any): ...

_SparseReshapeOutput = namedtuple('SparseReshape', ['output_indices', 'output_shape'])

def sparse_reshape(input_indices: Any, input_shape: Any, new_shape: Any, name: Optional[Any] = ...): ...

SparseReshape: Any

def sparse_reshape_eager_fallback(input_indices: Any, input_shape: Any, new_shape: Any, name: Any, ctx: Any): ...

_SparseSliceOutput = namedtuple('SparseSlice', ['output_indices', 'output_values', 'output_shape'])

def sparse_slice(indices: Any, values: Any, shape: Any, start: Any, size: Any, name: Optional[Any] = ...): ...

SparseSlice: Any

def sparse_slice_eager_fallback(indices: Any, values: Any, shape: Any, start: Any, size: Any, name: Any, ctx: Any): ...
def sparse_slice_grad(backprop_val_grad: Any, input_indices: Any, input_start: Any, output_indices: Any, name: Optional[Any] = ...): ...

SparseSliceGrad: Any

def sparse_slice_grad_eager_fallback(backprop_val_grad: Any, input_indices: Any, input_start: Any, output_indices: Any, name: Any, ctx: Any): ...
def sparse_softmax(sp_indices: Any, sp_values: Any, sp_shape: Any, name: Optional[Any] = ...): ...

SparseSoftmax: Any

def sparse_softmax_eager_fallback(sp_indices: Any, sp_values: Any, sp_shape: Any, name: Any, ctx: Any): ...

_SparseSparseMaximumOutput = namedtuple('SparseSparseMaximum', ['output_indices', 'output_values'])

def sparse_sparse_maximum(a_indices: Any, a_values: Any, a_shape: Any, b_indices: Any, b_values: Any, b_shape: Any, name: Optional[Any] = ...): ...

SparseSparseMaximum: Any

def sparse_sparse_maximum_eager_fallback(a_indices: Any, a_values: Any, a_shape: Any, b_indices: Any, b_values: Any, b_shape: Any, name: Any, ctx: Any): ...

_SparseSparseMinimumOutput = namedtuple('SparseSparseMinimum', ['output_indices', 'output_values'])

def sparse_sparse_minimum(a_indices: Any, a_values: Any, a_shape: Any, b_indices: Any, b_values: Any, b_shape: Any, name: Optional[Any] = ...): ...

SparseSparseMinimum: Any

def sparse_sparse_minimum_eager_fallback(a_indices: Any, a_values: Any, a_shape: Any, b_indices: Any, b_values: Any, b_shape: Any, name: Any, ctx: Any): ...

_SparseSplitOutput = namedtuple('SparseSplit', ['output_indices', 'output_values', 'output_shape'])

def sparse_split(split_dim: Any, indices: Any, values: Any, shape: Any, num_split: Any, name: Optional[Any] = ...): ...

SparseSplit: Any

def sparse_split_eager_fallback(split_dim: Any, indices: Any, values: Any, shape: Any, num_split: Any, name: Any, ctx: Any): ...
def sparse_tensor_dense_add(a_indices: Any, a_values: Any, a_shape: Any, b: Any, name: Optional[Any] = ...): ...

SparseTensorDenseAdd: Any

def sparse_tensor_dense_add_eager_fallback(a_indices: Any, a_values: Any, a_shape: Any, b: Any, name: Any, ctx: Any): ...
def sparse_tensor_dense_mat_mul(a_indices: Any, a_values: Any, a_shape: Any, b: Any, adjoint_a: bool = ..., adjoint_b: bool = ..., name: Optional[Any] = ...): ...

SparseTensorDenseMatMul: Any

def sparse_tensor_dense_mat_mul_eager_fallback(a_indices: Any, a_values: Any, a_shape: Any, b: Any, adjoint_a: Any, adjoint_b: Any, name: Any, ctx: Any): ...
def sparse_to_dense(sparse_indices: Any, output_shape: Any, sparse_values: Any, default_value: Any, validate_indices: bool = ..., name: Optional[Any] = ...): ...

SparseToDense: Any

def sparse_to_dense_eager_fallback(sparse_indices: Any, output_shape: Any, sparse_values: Any, default_value: Any, validate_indices: Any, name: Any, ctx: Any): ...

_TakeManySparseFromTensorsMapOutput = namedtuple('TakeManySparseFromTensorsMap', ['sparse_indices', 'sparse_values', 'sparse_shape'])

def take_many_sparse_from_tensors_map(sparse_handles: Any, dtype: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

TakeManySparseFromTensorsMap: Any

def take_many_sparse_from_tensors_map_eager_fallback(sparse_handles: Any, dtype: Any, container: Any, shared_name: Any, name: Any, ctx: Any): ...
