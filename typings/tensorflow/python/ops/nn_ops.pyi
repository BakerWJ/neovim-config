from tensorflow.python.ops.gen_nn_ops import *
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, graph_util as graph_util, ops as ops, random_seed as random_seed, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, gen_math_ops as gen_math_ops, gen_nn_ops as gen_nn_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.platform import device_context as device_context
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args, deprecated_argument_lookup as deprecated_argument_lookup
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

local_response_normalization = gen_nn_ops.lrn

class _NonAtrousConvolution:
    padding: Any = ...
    name: Any = ...
    strides: Any = ...
    data_format: Any = ...
    conv_op: Any = ...
    def __init__(self, input_shape: Any, filter_shape: Any, padding: Any, data_format: Optional[Any] = ..., strides: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def __call__(self, inp: Any, filter: Any): ...

def dilation2d_v2(input: Any, filters: Any, strides: Any, padding: Any, data_format: Any, dilations: Any, name: Optional[Any] = ...): ...
def dilation2d_v1(input: Any, filter: Optional[Any] = ..., strides: Optional[Any] = ..., rates: Optional[Any] = ..., padding: Optional[Any] = ..., name: Optional[Any] = ..., filters: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def with_space_to_batch(input: Any, dilation_rate: Any, padding: Any, op: Any, filter_shape: Optional[Any] = ..., spatial_dims: Optional[Any] = ..., data_format: Optional[Any] = ...): ...

class _WithSpaceToBatch:
    call: Any = ...
    base_paddings: Any = ...
    num_spatial_dims: Any = ...
    rate_or_const_rate: Any = ...
    input_shape: Any = ...
    spatial_dims: Any = ...
    dilation_rate: Any = ...
    data_format: Any = ...
    op: Any = ...
    def __init__(self, input_shape: Any, dilation_rate: Any, padding: Any, build_op: Any, filter_shape: Optional[Any] = ..., spatial_dims: Optional[Any] = ..., data_format: Optional[Any] = ...) -> None: ...
    def __call__(self, inp: Any, filter: Any): ...

def convolution(input: Any, filter: Any, padding: Any, strides: Optional[Any] = ..., dilation_rate: Optional[Any] = ..., name: Optional[Any] = ..., data_format: Optional[Any] = ..., filters: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def convolution_v2(input: Any, filters: Any, strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def convolution_internal(input: Any, filters: Any, strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ..., call_from_convolution: bool = ...): ...

class Convolution:
    input_shape: Any = ...
    filter_shape: Any = ...
    data_format: Any = ...
    strides: Any = ...
    padding: Any = ...
    name: Any = ...
    dilation_rate: Any = ...
    conv_op: Any = ...
    def __init__(self, input_shape: Any, filter_shape: Any, padding: Any, strides: Optional[Any] = ..., dilation_rate: Optional[Any] = ..., name: Optional[Any] = ..., data_format: Optional[Any] = ...) -> None: ...
    def __call__(self, inp: Any, filter: Any): ...

def pool(input: Any, window_shape: Any, pooling_type: Any, padding: Any, dilation_rate: Optional[Any] = ..., strides: Optional[Any] = ..., name: Optional[Any] = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def pool_v2(input: Any, window_shape: Any, pooling_type: Any, strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def atrous_conv2d(value: Any, filters: Any, rate: Any, padding: Any, name: Optional[Any] = ...): ...
def conv1d(value: Optional[Any] = ..., filters: Optional[Any] = ..., stride: Optional[Any] = ..., padding: Optional[Any] = ..., use_cudnn_on_gpu: Optional[Any] = ..., data_format: Optional[Any] = ..., name: Optional[Any] = ..., input: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def conv1d_v2(input: Any, filters: Any, stride: Any, padding: Any, data_format: str = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def conv1d_transpose(input: Any, filters: Any, output_shape: Any, strides: Any, padding: str = ..., data_format: str = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def conv2d_v2(input: Any, filters: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def conv2d(input: Any, filter: Optional[Any] = ..., strides: Optional[Any] = ..., padding: Optional[Any] = ..., use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., filters: Optional[Any] = ...): ...
def conv2d_backprop_filter(input: Any, filter_sizes: Any, out_backprop: Any, strides: Any, padding: Any, use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ...): ...
def conv2d_backprop_input(input_sizes: Any, filter: Optional[Any] = ..., out_backprop: Optional[Any] = ..., strides: Optional[Any] = ..., padding: Optional[Any] = ..., use_cudnn_on_gpu: bool = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., filters: Optional[Any] = ...): ...
def conv2d_transpose(value: Optional[Any] = ..., filter: Optional[Any] = ..., output_shape: Optional[Any] = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: str = ..., name: Optional[Any] = ..., input: Optional[Any] = ..., filters: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def conv2d_transpose_v2(input: Any, filters: Any, output_shape: Any, strides: Any, padding: str = ..., data_format: str = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def atrous_conv2d_transpose(value: Any, filters: Any, output_shape: Any, rate: Any, padding: Any, name: Optional[Any] = ...): ...
def conv3d_v2(input: Any, filters: Any, strides: Any, padding: Any, data_format: str = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def conv3d_v1(input: Any, filter: Optional[Any] = ..., strides: Optional[Any] = ..., padding: Optional[Any] = ..., data_format: str = ..., dilations: Any = ..., name: Optional[Any] = ..., filters: Optional[Any] = ...): ...
def conv3d_transpose(value: Any, filter: Optional[Any] = ..., output_shape: Optional[Any] = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: str = ..., name: Optional[Any] = ..., input: Optional[Any] = ..., filters: Optional[Any] = ..., dilations: Optional[Any] = ...): ...
def conv3d_transpose_v2(input: Any, filters: Any, output_shape: Any, strides: Any, padding: str = ..., data_format: str = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...

CONV_TRANSPOSE_OPS: Any

def conv_transpose(input: Any, filters: Any, output_shape: Any, strides: Any, padding: str = ..., data_format: Optional[Any] = ..., dilations: Optional[Any] = ..., name: Optional[Any] = ...): ...
def bias_add(value: Any, bias: Any, data_format: Optional[Any] = ..., name: Optional[Any] = ...): ...
def bias_add_v1(value: Any, bias: Any, name: Optional[Any] = ...): ...
def crelu(features: Any, name: Optional[Any] = ..., axis: int = ...): ...
def crelu_v2(features: Any, axis: int = ..., name: Optional[Any] = ...): ...
def relu6(features: Any, name: Optional[Any] = ...): ...
def leaky_relu(features: Any, alpha: float = ..., name: Optional[Any] = ...): ...
def softmax(logits: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., dim: Optional[Any] = ...): ...
def softmax_v2(logits: Any, axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
def log_softmax(logits: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., dim: Optional[Any] = ...): ...
def log_softmax_v2(logits: Any, axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
def softmax_cross_entropy_with_logits_v2(labels: Any, logits: Any, axis: int = ..., name: Optional[Any] = ...): ...
def softmax_cross_entropy_with_logits_v2_helper(labels: Any, logits: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., dim: Optional[Any] = ...): ...
def softmax_cross_entropy_with_logits(_sentinel: Optional[Any] = ..., labels: Optional[Any] = ..., logits: Optional[Any] = ..., dim: int = ..., name: Optional[Any] = ..., axis: Optional[Any] = ...): ...
def sparse_softmax_cross_entropy_with_logits(_sentinel: Optional[Any] = ..., labels: Optional[Any] = ..., logits: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sparse_softmax_cross_entropy_with_logits_v2(labels: Any, logits: Any, name: Optional[Any] = ...): ...
def avg_pool_v2(input: Any, ksize: Any, strides: Any, padding: Any, data_format: Optional[Any] = ..., name: Optional[Any] = ...): ...
def avg_pool(value: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., input: Optional[Any] = ...): ...
def avg_pool2d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def avg_pool1d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def avg_pool3d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_v2(input: Any, ksize: Any, strides: Any, padding: Any, data_format: Optional[Any] = ..., name: Optional[Any] = ...): ...
def max_pool(value: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ..., input: Optional[Any] = ...): ...
def max_pool1d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool2d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool3d(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def max_pool_with_argmax_v2(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., output_dtype: Any = ..., include_batch_in_index: bool = ..., name: Optional[Any] = ...): ...
def max_pool_with_argmax_v1(input: Any, ksize: Any, strides: Any, padding: Any, data_format: str = ..., Targmax: Optional[Any] = ..., name: Optional[Any] = ..., output_dtype: Optional[Any] = ..., include_batch_in_index: bool = ...): ...
def xw_plus_b(x: Any, weights: Any, biases: Any, name: Optional[Any] = ...): ...
def xw_plus_b_v1(x: Any, weights: Any, biases: Any, name: Optional[Any] = ...): ...
def dropout(x: Any, keep_prob: Optional[Any] = ..., noise_shape: Optional[Any] = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., rate: Optional[Any] = ...): ...
def dropout_v2(x: Any, rate: Any, noise_shape: Optional[Any] = ..., seed: Optional[Any] = ..., name: Optional[Any] = ...): ...
def top_k(input: Any, k: int = ..., sorted: bool = ..., name: Optional[Any] = ...): ...
def nth_element(input: Any, n: Any, reverse: bool = ..., name: Optional[Any] = ...): ...
def fractional_max_pool(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...
def fractional_max_pool_v2(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., seed: int = ..., name: Optional[Any] = ...): ...
def fractional_avg_pool(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...
def fractional_avg_pool_v2(value: Any, pooling_ratio: Any, pseudo_random: bool = ..., overlapping: bool = ..., seed: int = ..., name: Optional[Any] = ...): ...
def erosion2d(value: Any, kernel: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ...): ...
def erosion2d_v2(value: Any, filters: Any, strides: Any, padding: Any, data_format: Any, dilations: Any, name: Optional[Any] = ...): ...
def in_top_k(predictions: Any, targets: Any, k: Any, name: Optional[Any] = ...): ...
def in_top_k_v2(targets: Any, predictions: Any, k: Any, name: Optional[Any] = ...): ...
