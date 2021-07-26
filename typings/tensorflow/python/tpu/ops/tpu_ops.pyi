from tensorflow.python.ops.gen_tpu_ops import *
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_tpu_ops as gen_tpu_ops
from tensorflow.python.tpu import tpu_function as tpu_function
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def all_to_all(x: Any, concat_dimension: Any, split_dimension: Any, split_count: Any, group_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
def cross_replica_sum(x: Any, group_assignment: Optional[Any] = ..., name: Optional[Any] = ...): ...
def collective_permute(x: Any, source_target_pairs: Any, name: Optional[Any] = ...): ...
def infeed_dequeue(dtype: Any, shape: Any, name: Optional[Any] = ...): ...
def infeed_dequeue_tuple(dtypes: Any, shapes: Any, name: Optional[Any] = ...): ...
def send_tpu_embedding_gradients(inputs: Any, config: Any, learning_rates: Optional[Any] = ..., name: Optional[Any] = ...): ...
def enqueue_tpu_embedding_integer_batch(batch: Any, device_ordinal: Any, mode_override: Optional[Any] = ..., name: Optional[Any] = ...): ...
def enqueue_tpu_embedding_sparse_batch(sample_indices: Any, embedding_indices: Any, aggregation_weights: Any, device_ordinal: Any, combiners: Optional[Any] = ..., mode_override: Optional[Any] = ..., name: Optional[Any] = ...): ...
def enqueue_tpu_embedding_sparse_tensor_batch(sample_indices: Any, embedding_indices: Any, aggregation_weights: Any, table_ids: Any, device_ordinal: Any, max_sequence_lengths: Optional[Any] = ..., combiners: Optional[Any] = ..., mode_override: Optional[Any] = ..., name: Optional[Any] = ...): ...
