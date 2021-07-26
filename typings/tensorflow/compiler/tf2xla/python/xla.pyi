from tensorflow.compiler.tf2xla.ops import gen_xla_ops as gen_xla_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, bitwise_ops as bitwise_ops, gen_math_ops as gen_math_ops, gen_random_ops as gen_random_ops, math_ops as math_ops, random_ops as random_ops
from typing import Any, Optional

constant: Any
abs: Any
conj: Any
cos: Any
ceil: Any
digamma: Any
erf: Any
erfc: Any
erfinv: Any
ndtri: Any
exp: Any
expm1: Any
floor: Any
imag: Any
is_finite: Any
lgamma: Any
log: Any
log1p: Any
logical_not: Any
neg: Any
real: Any
round: Any
sin: Any
sign: Any
tanh: Any
bessel_i0e: Any
bessel_i1e: Any
add: Any
sub: Any
mul: Any
div: Any
rem: Any
max: Any
min: Any
atan2: Any
complex: Any
logical_and: Any
logical_or: Any
logical_xor: Any
eq: Any
ne: Any
ge: Any
gt: Any
le: Any
lt: Any
pow: Any
shift_left: Any
shift_right_logical: Any
shift_right_arithmetic: Any
igamma: Any
igamma_grad_a: Any
random_gamma_grad: Any
igammac: Any
transpose: Any
rev: Any
bitcast_convert_type: Any

def broadcast(x: Any, dims: Any, name: Optional[Any] = ...): ...
def clamp(a: Any, x: Any, b: Any, name: Optional[Any] = ...): ...

concatenate: Any

def conv(lhs: Any, rhs: Any, window_strides: Any, padding: Any, lhs_dilation: Any, rhs_dilation: Any, dimension_numbers: Any, feature_group_count: int = ..., precision_config: Optional[Any] = ..., name: Optional[Any] = ...): ...

convert_element_type: Any

def dot(lhs: Any, rhs: Any, name: Optional[Any] = ...): ...
def dot_general(lhs: Any, rhs: Any, dimension_numbers: Any, precision_config: Optional[Any] = ..., name: Optional[Any] = ...): ...
def self_adjoint_eig(a: Any, lower: Any, max_iter: Any, epsilon: Any): ...
def svd(a: Any, max_iter: Any, epsilon: Any, precision_config: Optional[Any] = ...): ...

dynamic_slice: Any
dynamic_update_slice: Any
einsum: Any
pad: Any

def random_normal(mu: Any, sigma: Any, dims: Any, name: Optional[Any] = ...): ...
def random_uniform(minval: Any, maxval: Any, dims: Any, name: Optional[Any] = ...): ...

recv: Any
reduce: Any

def reduce_window(operand: Any, init: Any, reducer: Any, window_dimensions: Any, window_strides: Optional[Any] = ..., base_dilations: Optional[Any] = ..., window_dilations: Optional[Any] = ..., padding: Optional[Any] = ..., name: Optional[Any] = ...): ...

replica_id: Any

def reshape(x: Any, new_sizes: Any, dimensions: Optional[Any] = ..., name: Optional[Any] = ...): ...
def select(condition: Any, x: Any, y: Any, name: Optional[Any] = ...): ...

select_and_scatter: Any
send: Any

def slice(x: Any, start_dims: Any, limit_dims: Any, strides: Any): ...

sharding: Any
sort: Any
key_value_sort: Any
while_loop: Any
dequantize: Any

def gather(operand: Any, start_indices: Any, dimension_numbers: Any, slice_sizes: Any, indices_are_sorted: bool = ..., name: Optional[Any] = ...): ...
def scatter(operand: Any, scatter_indices: Any, updates: Any, update_computation: Any, dimension_numbers: Any, indices_are_sorted: bool = ..., name: Optional[Any] = ...): ...
