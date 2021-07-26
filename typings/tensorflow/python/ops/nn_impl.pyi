from tensorflow.python.compat import compat as compat
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, candidate_sampling_ops as candidate_sampling_ops, control_flow_ops as control_flow_ops, custom_gradient as custom_gradient, embedding_ops as embedding_ops, gen_array_ops as gen_array_ops, gen_nn_ops as gen_nn_ops, gen_sparse_ops as gen_sparse_ops, linalg_ops as linalg_ops, math_ops as math_ops, nn_ops as nn_ops, variables as variables
from tensorflow.python.platform import device_context as device_context
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args, deprecated_argument_lookup as deprecated_argument_lookup
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def log_poisson_loss(targets: Any, log_input: Any, compute_full_loss: bool = ..., name: Optional[Any] = ...): ...
def sigmoid_cross_entropy_with_logits(_sentinel: Optional[Any] = ..., labels: Optional[Any] = ..., logits: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sigmoid_cross_entropy_with_logits_v2(labels: Optional[Any] = ..., logits: Optional[Any] = ..., name: Optional[Any] = ...): ...
def weighted_cross_entropy_with_logits_v2(labels: Any, logits: Any, pos_weight: Any, name: Optional[Any] = ...): ...
def weighted_cross_entropy_with_logits(labels: Optional[Any] = ..., logits: Optional[Any] = ..., pos_weight: Optional[Any] = ..., name: Optional[Any] = ..., targets: Optional[Any] = ...): ...
def compute_average_loss(per_example_loss: Any, sample_weight: Optional[Any] = ..., global_batch_size: Optional[Any] = ...): ...
def scale_regularization_loss(regularization_loss: Any): ...
def relu_layer(x: Any, weights: Any, biases: Any, name: Optional[Any] = ...): ...
def swish(features: Any): ...
def normalize(tensor: Any, ord: str = ..., axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
def l2_normalize(x: Any, axis: Optional[Any] = ..., epsilon: float = ..., name: Optional[Any] = ..., dim: Optional[Any] = ...): ...
def l2_normalize_v2(x: Any, axis: Optional[Any] = ..., epsilon: float = ..., name: Optional[Any] = ...): ...
def zero_fraction(value: Any, name: Optional[Any] = ...): ...
def depthwise_conv2d(input: Any, filter: Any, strides: Any, padding: Any, rate: Optional[Any] = ..., name: Optional[Any] = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def depthwise_conv2d_v2(input: Any, filter: Any, strides: Any, padding: Any, data_format: Optional[Any] = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def separable_conv2d(input: Any, depthwise_filter: Any, pointwise_filter: Any, strides: Any, padding: Any, rate: Optional[Any] = ..., name: Optional[Any] = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def separable_conv2d_v2(input: Any, depthwise_filter: Any, pointwise_filter: Any, strides: Any, padding: Any, data_format: Optional[Any] = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sufficient_statistics(x: Any, axes: Any, shift: Optional[Any] = ..., keep_dims: Optional[Any] = ..., name: Optional[Any] = ..., keepdims: Optional[Any] = ...): ...
def sufficient_statistics_v2(x: Any, axes: Any, shift: Optional[Any] = ..., keepdims: bool = ..., name: Optional[Any] = ...): ...
def normalize_moments(counts: Any, mean_ss: Any, variance_ss: Any, shift: Any, name: Optional[Any] = ...): ...
def moments(x: Any, axes: Any, shift: Optional[Any] = ..., name: Optional[Any] = ..., keep_dims: Optional[Any] = ..., keepdims: Optional[Any] = ...): ...
def moments_v2(x: Any, axes: Any, shift: Optional[Any] = ..., keepdims: bool = ..., name: Optional[Any] = ...): ...
def weighted_moments(x: Any, axes: Any, frequency_weights: Any, name: Optional[Any] = ..., keep_dims: Optional[Any] = ..., keepdims: Optional[Any] = ...): ...
def weighted_moments_v2(x: Any, axes: Any, frequency_weights: Any, keepdims: bool = ..., name: Optional[Any] = ...): ...
def batch_normalization(x: Any, mean: Any, variance: Any, offset: Any, scale: Any, variance_epsilon: Any, name: Optional[Any] = ...): ...
def fused_batch_norm(x: Any, scale: Any, offset: Any, mean: Optional[Any] = ..., variance: Optional[Any] = ..., epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Optional[Any] = ..., exponential_avg_factor: float = ...): ...
def batch_norm_with_global_normalization(t: Optional[Any] = ..., m: Optional[Any] = ..., v: Optional[Any] = ..., beta: Optional[Any] = ..., gamma: Optional[Any] = ..., variance_epsilon: Optional[Any] = ..., scale_after_normalization: Optional[Any] = ..., name: Optional[Any] = ..., input: Optional[Any] = ..., mean: Optional[Any] = ..., variance: Optional[Any] = ...): ...
def batch_norm_with_global_normalization_v2(input: Any, mean: Any, variance: Any, beta: Any, gamma: Any, variance_epsilon: Any, scale_after_normalization: Any, name: Optional[Any] = ...): ...
def nce_loss_v2(weights: Any, biases: Any, labels: Any, inputs: Any, num_sampled: Any, num_classes: Any, num_true: int = ..., sampled_values: Optional[Any] = ..., remove_accidental_hits: bool = ..., name: str = ...): ...
def nce_loss(weights: Any, biases: Any, labels: Any, inputs: Any, num_sampled: Any, num_classes: Any, num_true: int = ..., sampled_values: Optional[Any] = ..., remove_accidental_hits: bool = ..., partition_strategy: str = ..., name: str = ...): ...
def sampled_softmax_loss_v2(weights: Any, biases: Any, labels: Any, inputs: Any, num_sampled: Any, num_classes: Any, num_true: int = ..., sampled_values: Optional[Any] = ..., remove_accidental_hits: bool = ..., seed: Optional[Any] = ..., name: str = ...): ...
def sampled_softmax_loss(weights: Any, biases: Any, labels: Any, inputs: Any, num_sampled: Any, num_classes: Any, num_true: int = ..., sampled_values: Optional[Any] = ..., remove_accidental_hits: bool = ..., partition_strategy: str = ..., name: str = ..., seed: Optional[Any] = ...): ...
