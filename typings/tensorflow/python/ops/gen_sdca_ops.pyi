from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def sdca_fprint(input: Any, name: Optional[Any] = ...): ...

SdcaFprint: Any

def sdca_fprint_eager_fallback(input: Any, name: Any, ctx: Any): ...

_SdcaOptimizerOutput = namedtuple('SdcaOptimizer', ['out_example_state_data', 'out_delta_sparse_weights', 'out_delta_dense_weights'])

def sdca_optimizer(sparse_example_indices: Any, sparse_feature_indices: Any, sparse_feature_values: Any, dense_features: Any, example_weights: Any, example_labels: Any, sparse_indices: Any, sparse_weights: Any, dense_weights: Any, example_state_data: Any, loss_type: Any, l1: Any, l2: Any, num_loss_partitions: Any, num_inner_iterations: Any, adaptative: bool = ..., name: Optional[Any] = ...): ...

SdcaOptimizer: Any

def sdca_optimizer_eager_fallback(sparse_example_indices: Any, sparse_feature_indices: Any, sparse_feature_values: Any, dense_features: Any, example_weights: Any, example_labels: Any, sparse_indices: Any, sparse_weights: Any, dense_weights: Any, example_state_data: Any, loss_type: Any, l1: Any, l2: Any, num_loss_partitions: Any, num_inner_iterations: Any, adaptative: Any, name: Any, ctx: Any): ...

_SdcaOptimizerV2Output = namedtuple('SdcaOptimizerV2', ['out_example_state_data', 'out_delta_sparse_weights', 'out_delta_dense_weights'])

def sdca_optimizer_v2(sparse_example_indices: Any, sparse_feature_indices: Any, sparse_feature_values: Any, dense_features: Any, example_weights: Any, example_labels: Any, sparse_indices: Any, sparse_weights: Any, dense_weights: Any, example_state_data: Any, loss_type: Any, l1: Any, l2: Any, num_loss_partitions: Any, num_inner_iterations: Any, adaptive: bool = ..., name: Optional[Any] = ...): ...

SdcaOptimizerV2: Any

def sdca_optimizer_v2_eager_fallback(sparse_example_indices: Any, sparse_feature_indices: Any, sparse_feature_values: Any, dense_features: Any, example_weights: Any, example_labels: Any, sparse_indices: Any, sparse_weights: Any, dense_weights: Any, example_state_data: Any, loss_type: Any, l1: Any, l2: Any, num_loss_partitions: Any, num_inner_iterations: Any, adaptive: Any, name: Any, ctx: Any): ...
def sdca_shrink_l1(weights: Any, l1: Any, l2: Any, name: Optional[Any] = ...): ...

SdcaShrinkL1: Any

def sdca_shrink_l1_eager_fallback(weights: Any, l1: Any, l2: Any, name: Any, ctx: Any) -> None: ...
