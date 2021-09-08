from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_XlaBroadcastHelperOutput = namedtuple('XlaBroadcastHelper', ['lhs_output', 'rhs_output'])

def xla_broadcast_helper(lhs: Any, rhs: Any, broadcast_dims: Any, name: Optional[Any] = ...): ...

XlaBroadcastHelper: Any

def xla_broadcast_helper_eager_fallback(lhs: Any, rhs: Any, broadcast_dims: Any, name: Any, ctx: Any): ...
def xla_conv(lhs: Any, rhs: Any, window_strides: Any, padding: Any, lhs_dilation: Any, rhs_dilation: Any, feature_group_count: Any, dimension_numbers: Any, precision_config: Any, name: Optional[Any] = ...): ...

XlaConv: Any

def xla_conv_eager_fallback(lhs: Any, rhs: Any, window_strides: Any, padding: Any, lhs_dilation: Any, rhs_dilation: Any, feature_group_count: Any, dimension_numbers: Any, precision_config: Any, name: Any, ctx: Any): ...
def xla_dequantize(input: Any, min_range: Any, max_range: Any, mode: Any, transpose_output: Any, name: Optional[Any] = ...): ...

XlaDequantize: Any

def xla_dequantize_eager_fallback(input: Any, min_range: Any, max_range: Any, mode: Any, transpose_output: Any, name: Any, ctx: Any): ...
def xla_dot(lhs: Any, rhs: Any, dimension_numbers: Any, precision_config: Any, name: Optional[Any] = ...): ...

XlaDot: Any

def xla_dot_eager_fallback(lhs: Any, rhs: Any, dimension_numbers: Any, precision_config: Any, name: Any, ctx: Any): ...
def xla_dynamic_slice(input: Any, start_indices: Any, size_indices: Any, name: Optional[Any] = ...): ...

XlaDynamicSlice: Any

def xla_dynamic_slice_eager_fallback(input: Any, start_indices: Any, size_indices: Any, name: Any, ctx: Any): ...
def xla_dynamic_update_slice(input: Any, update: Any, indices: Any, name: Optional[Any] = ...): ...

XlaDynamicUpdateSlice: Any

def xla_dynamic_update_slice_eager_fallback(input: Any, update: Any, indices: Any, name: Any, ctx: Any): ...
def xla_einsum(a: Any, b: Any, equation: Any, name: Optional[Any] = ...): ...

XlaEinsum: Any

def xla_einsum_eager_fallback(a: Any, b: Any, equation: Any, name: Any, ctx: Any): ...
def xla_gather(operand: Any, start_indices: Any, slice_sizes: Any, dimension_numbers: Any, indices_are_sorted: Any, name: Optional[Any] = ...): ...

XlaGather: Any

def xla_gather_eager_fallback(operand: Any, start_indices: Any, slice_sizes: Any, dimension_numbers: Any, indices_are_sorted: Any, name: Any, ctx: Any): ...
def xla_if(cond: Any, inputs: Any, then_branch: Any, else_branch: Any, Tout: Any, name: Optional[Any] = ...): ...

XlaIf: Any

def xla_if_eager_fallback(cond: Any, inputs: Any, then_branch: Any, else_branch: Any, Tout: Any, name: Any, ctx: Any): ...

_XlaKeyValueSortOutput = namedtuple('XlaKeyValueSort', ['sorted_keys', 'sorted_values'])

def xla_key_value_sort(keys: Any, values: Any, name: Optional[Any] = ...): ...

XlaKeyValueSort: Any

def xla_key_value_sort_eager_fallback(keys: Any, values: Any, name: Any, ctx: Any): ...
def xla_pad(input: Any, padding_value: Any, padding_low: Any, padding_high: Any, padding_interior: Any, name: Optional[Any] = ...): ...

XlaPad: Any

def xla_pad_eager_fallback(input: Any, padding_value: Any, padding_low: Any, padding_high: Any, padding_interior: Any, name: Any, ctx: Any): ...
def xla_recv(dtype: Any, tensor_name: Any, shape: Any, name: Optional[Any] = ...): ...

XlaRecv: Any

def xla_recv_eager_fallback(dtype: Any, tensor_name: Any, shape: Any, name: Any, ctx: Any): ...
def xla_reduce(input: Any, init_value: Any, dimensions_to_reduce: Any, reducer: Any, name: Optional[Any] = ...): ...

XlaReduce: Any

def xla_reduce_eager_fallback(input: Any, init_value: Any, dimensions_to_reduce: Any, reducer: Any, name: Any, ctx: Any): ...
def xla_reduce_window(input: Any, init_value: Any, window_dimensions: Any, window_strides: Any, base_dilations: Any, window_dilations: Any, padding: Any, computation: Any, name: Optional[Any] = ...): ...

XlaReduceWindow: Any

def xla_reduce_window_eager_fallback(input: Any, init_value: Any, window_dimensions: Any, window_strides: Any, base_dilations: Any, window_dilations: Any, padding: Any, computation: Any, name: Any, ctx: Any): ...
def xla_replica_id(name: Optional[Any] = ...): ...

XlaReplicaId: Any

def xla_replica_id_eager_fallback(name: Any, ctx: Any): ...
def xla_scatter(operand: Any, scatter_indices: Any, updates: Any, update_computation: Any, dimension_numbers: Any, indices_are_sorted: Any, name: Optional[Any] = ...): ...

XlaScatter: Any

def xla_scatter_eager_fallback(operand: Any, scatter_indices: Any, updates: Any, update_computation: Any, dimension_numbers: Any, indices_are_sorted: Any, name: Any, ctx: Any): ...
def xla_select_and_scatter(operand: Any, window_dimensions: Any, window_strides: Any, padding: Any, source: Any, init_value: Any, select: Any, scatter: Any, name: Optional[Any] = ...): ...

XlaSelectAndScatter: Any

def xla_select_and_scatter_eager_fallback(operand: Any, window_dimensions: Any, window_strides: Any, padding: Any, source: Any, init_value: Any, select: Any, scatter: Any, name: Any, ctx: Any): ...

_XlaSelfAdjointEigOutput = namedtuple('XlaSelfAdjointEig', ['w', 'v'])

def xla_self_adjoint_eig(a: Any, lower: Any, max_iter: Any, epsilon: Any, name: Optional[Any] = ...): ...

XlaSelfAdjointEig: Any

def xla_self_adjoint_eig_eager_fallback(a: Any, lower: Any, max_iter: Any, epsilon: Any, name: Any, ctx: Any): ...
def xla_send(tensor: Any, tensor_name: Any, name: Optional[Any] = ...): ...

XlaSend: Any

def xla_send_eager_fallback(tensor: Any, tensor_name: Any, name: Any, ctx: Any): ...
def xla_sharding(input: Any, name: Optional[Any] = ...): ...

XlaSharding: Any

def xla_sharding_eager_fallback(input: Any, name: Any, ctx: Any): ...
def xla_sort(input: Any, name: Optional[Any] = ...): ...

XlaSort: Any

def xla_sort_eager_fallback(input: Any, name: Any, ctx: Any): ...

_XlaSvdOutput = namedtuple('XlaSvd', ['s', 'u', 'v'])

def xla_svd(a: Any, max_iter: Any, epsilon: Any, precision_config: Any, name: Optional[Any] = ...): ...

XlaSvd: Any

def xla_svd_eager_fallback(a: Any, max_iter: Any, epsilon: Any, precision_config: Any, name: Any, ctx: Any): ...
def xla_while(input: Any, cond: Any, body: Any, name: Optional[Any] = ...): ...

XlaWhile: Any

def xla_while_eager_fallback(input: Any, cond: Any, body: Any, name: Any, ctx: Any): ...