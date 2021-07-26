from tensorflow.python.ops.gen_array_ops import *
from tensorflow.python.eager import context as context
from tensorflow.python.framework import common_shapes as common_shapes, composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.framework.constant_op import constant as constant
from tensorflow.python.ops import gen_array_ops as gen_array_ops, gen_math_ops as gen_math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch, nest as nest, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

newaxis: Any

def reshape(tensor: Any, shape: Any, name: Optional[Any] = ...): ...
def fill(dims: Any, value: Any, name: Optional[Any] = ...): ...
def identity(input: Any, name: Optional[Any] = ...): ...
def expand_dims(input: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., dim: Optional[Any] = ...): ...
def expand_dims_v2(input: Any, axis: Any, name: Optional[Any] = ...): ...
def listdiff(x: Any, y: Any, out_idx: Optional[Any] = ..., name: Optional[Any] = ...): ...
def setdiff1d(x: Any, y: Any, index_dtype: Any = ..., name: Optional[Any] = ...): ...
def broadcast_dynamic_shape(shape_x: Any, shape_y: Any): ...
def broadcast_static_shape(shape_x: Any, shape_y: Any): ...
def shape_v2(input: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def shape(input: Any, name: Optional[Any] = ..., out_type: Any = ...): ...
def shape_internal(input: Any, name: Optional[Any] = ..., optimize: bool = ..., out_type: Any = ...): ...
def shape_n(input: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def size_v2(input: Any, out_type: Any = ..., name: Optional[Any] = ...): ...
def size(input: Any, name: Optional[Any] = ..., out_type: Any = ...): ...
def size_internal(input: Any, name: Optional[Any] = ..., optimize: bool = ..., out_type: Any = ...): ...
def rank(input: Any, name: Optional[Any] = ...): ...
def rank_internal(input: Any, name: Optional[Any] = ..., optimize: bool = ...): ...
def slice(input_: Any, begin: Any, size: Any, name: Optional[Any] = ...): ...
def strided_slice(input_: Any, begin: Any, end: Any, strides: Optional[Any] = ..., begin_mask: int = ..., end_mask: int = ..., ellipsis_mask: int = ..., new_axis_mask: int = ..., shrink_axis_mask: int = ..., var: Optional[Any] = ..., name: Optional[Any] = ...): ...
def parallel_stack(values: Any, name: str = ...): ...
def stack(values: Any, axis: int = ..., name: str = ...): ...
def unstack(value: Any, num: Optional[Any] = ..., axis: int = ..., name: str = ...): ...
def concat(values: Any, axis: Any, name: str = ...): ...
def boolean_mask(tensor: Any, mask: Any, name: str = ..., axis: Optional[Any] = ...): ...
def boolean_mask_v2(tensor: Any, mask: Any, axis: Optional[Any] = ..., name: str = ...): ...
def sparse_mask(a: Any, mask_indices: Any, name: Optional[Any] = ...): ...
def unique(x: Any, out_idx: Any = ..., name: Optional[Any] = ...): ...
def unique_with_counts(x: Any, out_idx: Any = ..., name: Optional[Any] = ...): ...
def split(value: Any, num_or_size_splits: Any, axis: int = ..., num: Optional[Any] = ..., name: str = ...): ...
def transpose_v2(a: Any, perm: Optional[Any] = ..., conjugate: bool = ..., name: str = ...): ...
def transpose(a: Any, perm: Optional[Any] = ..., name: str = ..., conjugate: bool = ...): ...
def matrix_transpose(a: Any, name: str = ..., conjugate: bool = ...): ...
def matrix_diag(diagonal: Any, name: str = ..., k: int = ..., num_rows: int = ..., num_cols: int = ..., padding_value: int = ..., align: str = ...): ...
def matrix_diag_part(input: Any, name: str = ..., k: int = ..., padding_value: int = ..., align: str = ...): ...
def matrix_set_diag(input: Any, diagonal: Any, name: str = ..., k: int = ..., align: str = ...): ...
def zeros(shape: Any, dtype: Any = ..., name: Optional[Any] = ...): ...
def zeros_like(tensor: Any, dtype: Optional[Any] = ..., name: Optional[Any] = ..., optimize: bool = ...): ...
def zeros_like_v2(input: Any, dtype: Optional[Any] = ..., name: Optional[Any] = ...): ...
def zeros_like_impl(tensor: Any, dtype: Any, name: Any, optimize: bool = ...): ...
def ones_like(tensor: Any, dtype: Optional[Any] = ..., name: Optional[Any] = ..., optimize: bool = ...): ...
def ones_like_v2(input: Any, dtype: Optional[Any] = ..., name: Optional[Any] = ...): ...
def ones_like_impl(tensor: Any, dtype: Any, name: Any, optimize: bool = ...): ...
def ones(shape: Any, dtype: Any = ..., name: Optional[Any] = ...): ...
def placeholder(dtype: Any, shape: Optional[Any] = ..., name: Optional[Any] = ...): ...
def placeholder_with_default(input: Any, shape: Any, name: Optional[Any] = ...): ...
def sparse_placeholder(dtype: Any, shape: Optional[Any] = ..., name: Optional[Any] = ...): ...
def pad_v2(tensor: Any, paddings: Any, mode: str = ..., constant_values: int = ..., name: Optional[Any] = ...): ...
def pad(tensor: Any, paddings: Any, mode: str = ..., name: Optional[Any] = ..., constant_values: int = ...): ...
def meshgrid(*args: Any, **kwargs: Any): ...

NEW_AXIS: int
SHRINK_AXIS: int

def edit_distance(hypothesis: Any, truth: Any, normalize: bool = ..., name: str = ...): ...
def required_space_to_batch_paddings(input_shape: Any, block_shape: Any, base_paddings: Optional[Any] = ..., name: Optional[Any] = ...): ...
def space_to_batch(input: Any, paddings: Any, block_size: Optional[Any] = ..., name: Optional[Any] = ..., block_shape: Optional[Any] = ...): ...
def space_to_batch_v2(input: Any, block_shape: Any, paddings: Any, name: Optional[Any] = ...): ...
def space_to_depth(input: Any, block_size: Any, name: Optional[Any] = ..., data_format: str = ...): ...
def space_to_depth_v2(input: Any, block_size: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def depth_to_space(input: Any, block_size: Any, name: Optional[Any] = ..., data_format: str = ...): ...
def depth_to_space_v2(input: Any, block_size: Any, data_format: str = ..., name: Optional[Any] = ...): ...
def batch_to_space(input: Any, crops: Any, block_size: Any, name: Optional[Any] = ..., block_shape: Optional[Any] = ...): ...
def batch_to_space_v2(input: Any, block_shape: Any, crops: Any, name: Optional[Any] = ...): ...
def one_hot(indices: Any, depth: Any, on_value: Optional[Any] = ..., off_value: Optional[Any] = ..., axis: Optional[Any] = ..., dtype: Optional[Any] = ..., name: Optional[Any] = ...): ...
def sequence_mask(lengths: Any, maxlen: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
def squeeze(input: Any, axis: Optional[Any] = ..., name: Optional[Any] = ..., squeeze_dims: Optional[Any] = ...): ...
def squeeze_v2(input: Any, axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
def where(condition: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., name: Optional[Any] = ...): ...
def where_v2(condition: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., name: Optional[Any] = ...): ...
def reverse_sequence(input: Any, seq_lengths: Any, seq_axis: Optional[Any] = ..., batch_axis: Optional[Any] = ..., name: Optional[Any] = ..., seq_dim: Optional[Any] = ..., batch_dim: Optional[Any] = ...): ...
def reverse_sequence_v2(input: Any, seq_lengths: Any, seq_axis: Optional[Any] = ..., batch_axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
def gather(params: Any, indices: Any, validate_indices: Optional[Any] = ..., name: Optional[Any] = ..., axis: Optional[Any] = ..., batch_dims: int = ...): ...
def gather_v2(params: Any, indices: Any, validate_indices: Optional[Any] = ..., axis: Optional[Any] = ..., batch_dims: int = ..., name: Optional[Any] = ...): ...
def batch_gather(params: Any, indices: Any, name: Optional[Any] = ...): ...
def gather_nd(params: Any, indices: Any, name: Optional[Any] = ..., batch_dims: int = ...): ...
def gather_nd_v2(params: Any, indices: Any, batch_dims: int = ..., name: Optional[Any] = ...): ...
def batch_gather_nd(params: Any, indices: Any, batch_dims: Any, name: Optional[Any] = ...): ...
def quantize_v2(input: Any, min_range: Any, max_range: Any, T: Any, mode: str = ..., name: Optional[Any] = ..., round_mode: str = ..., narrow_range: bool = ..., axis: Optional[Any] = ..., ensure_minimum_range: float = ...): ...
def quantize(input: Any, min_range: Any, max_range: Any, T: Any, mode: str = ..., round_mode: str = ..., name: Optional[Any] = ..., narrow_range: bool = ..., axis: Optional[Any] = ..., ensure_minimum_range: float = ...): ...
def dequantize(input: Any, min_range: Any, max_range: Any, mode: str = ..., name: Optional[Any] = ..., axis: Optional[Any] = ..., narrow_range: bool = ..., dtype: Any = ...): ...
def quantize_and_dequantize(input: Any, input_min: Any, input_max: Any, signed_input: bool = ..., num_bits: int = ..., range_given: bool = ..., round_mode: str = ..., name: Optional[Any] = ..., narrow_range: bool = ..., axis: Optional[Any] = ...): ...
def searchsorted(sorted_sequence: Any, values: Any, side: str = ..., out_type: Any = ..., name: Optional[Any] = ...): ...
def extract_image_patches_v2(images: Any, sizes: Any, strides: Any, rates: Any, padding: Any, name: Optional[Any] = ...): ...
def extract_image_patches(images: Any, ksizes: Optional[Any] = ..., strides: Optional[Any] = ..., rates: Optional[Any] = ..., padding: Optional[Any] = ..., name: Optional[Any] = ..., sizes: Optional[Any] = ...): ...
def fingerprint(data: Any, method: str = ..., name: Optional[Any] = ...): ...
def convert_to_int_tensor(tensor: Any, name: Any, dtype: Any = ...): ...
def get_positive_axis(axis: Any, ndims: Any, axis_name: str = ..., ndims_name: str = ...): ...
def repeat_with_axis(data: Any, repeats: Any, axis: Any, name: Optional[Any] = ...): ...
def tile_one_dimension(data: Any, axis: Any, multiple: Any): ...
def repeat(input: Any, repeats: Any, axis: Optional[Any] = ..., name: Optional[Any] = ...): ...
