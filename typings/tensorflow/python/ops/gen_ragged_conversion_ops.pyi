from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_RaggedTensorFromVariantOutput = namedtuple('RaggedTensorFromVariant', ['output_nested_splits', 'output_dense_values'])

def ragged_tensor_from_variant(encoded_ragged: Any, input_ragged_rank: Any, output_ragged_rank: Any, Tvalues: Any, Tsplits: Any = ..., name: Optional[Any] = ...): ...

RaggedTensorFromVariant: Any

def ragged_tensor_from_variant_eager_fallback(encoded_ragged: Any, input_ragged_rank: Any, output_ragged_rank: Any, Tvalues: Any, Tsplits: Any, name: Any, ctx: Any): ...

_RaggedTensorToSparseOutput = namedtuple('RaggedTensorToSparse', ['sparse_indices', 'sparse_values', 'sparse_dense_shape'])

def ragged_tensor_to_sparse(rt_nested_splits: Any, rt_dense_values: Any, name: Optional[Any] = ...): ...

RaggedTensorToSparse: Any

def ragged_tensor_to_sparse_eager_fallback(rt_nested_splits: Any, rt_dense_values: Any, name: Any, ctx: Any): ...
def ragged_tensor_to_tensor(shape: Any, values: Any, default_value: Any, row_partition_tensors: Any, row_partition_types: Any, name: Optional[Any] = ...): ...

RaggedTensorToTensor: Any

def ragged_tensor_to_tensor_eager_fallback(shape: Any, values: Any, default_value: Any, row_partition_tensors: Any, row_partition_types: Any, name: Any, ctx: Any): ...
def ragged_tensor_to_variant(rt_nested_splits: Any, rt_dense_values: Any, batched_input: Any, name: Optional[Any] = ...): ...

RaggedTensorToVariant: Any

def ragged_tensor_to_variant_eager_fallback(rt_nested_splits: Any, rt_dense_values: Any, batched_input: Any, name: Any, ctx: Any): ...
