from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def empty_tensor_list(element_shape: Any, max_num_elements: Any, element_dtype: Any, name: Optional[Any] = ...): ...

EmptyTensorList: Any

def empty_tensor_list_eager_fallback(element_shape: Any, max_num_elements: Any, element_dtype: Any, name: Any, ctx: Any): ...

_TensorListConcatOutput = namedtuple('TensorListConcat', ['tensor', 'lengths'])

def tensor_list_concat(input_handle: Any, element_dtype: Any, element_shape: Optional[Any] = ..., name: Optional[Any] = ...): ...

TensorListConcat: Any

def tensor_list_concat_eager_fallback(input_handle: Any, element_dtype: Any, element_shape: Any, name: Any, ctx: Any): ...
def tensor_list_concat_lists(input_a: Any, input_b: Any, element_dtype: Any, name: Optional[Any] = ...): ...

TensorListConcatLists: Any

def tensor_list_concat_lists_eager_fallback(input_a: Any, input_b: Any, element_dtype: Any, name: Any, ctx: Any): ...

_TensorListConcatV2Output = namedtuple('TensorListConcatV2', ['tensor', 'lengths'])

def tensor_list_concat_v2(input_handle: Any, element_shape: Any, leading_dims: Any, element_dtype: Any, name: Optional[Any] = ...): ...

TensorListConcatV2: Any

def tensor_list_concat_v2_eager_fallback(input_handle: Any, element_shape: Any, leading_dims: Any, element_dtype: Any, name: Any, ctx: Any): ...
def tensor_list_element_shape(input_handle: Any, shape_type: Any, name: Optional[Any] = ...): ...

TensorListElementShape: Any

def tensor_list_element_shape_eager_fallback(input_handle: Any, shape_type: Any, name: Any, ctx: Any): ...
def tensor_list_from_tensor(tensor: Any, element_shape: Any, name: Optional[Any] = ...): ...

TensorListFromTensor: Any

def tensor_list_from_tensor_eager_fallback(tensor: Any, element_shape: Any, name: Any, ctx: Any): ...
def tensor_list_gather(input_handle: Any, indices: Any, element_shape: Any, element_dtype: Any, name: Optional[Any] = ...): ...

TensorListGather: Any

def tensor_list_gather_eager_fallback(input_handle: Any, indices: Any, element_shape: Any, element_dtype: Any, name: Any, ctx: Any): ...
def tensor_list_get_item(input_handle: Any, index: Any, element_shape: Any, element_dtype: Any, name: Optional[Any] = ...): ...

TensorListGetItem: Any

def tensor_list_get_item_eager_fallback(input_handle: Any, index: Any, element_shape: Any, element_dtype: Any, name: Any, ctx: Any): ...
def tensor_list_length(input_handle: Any, name: Optional[Any] = ...): ...

TensorListLength: Any

def tensor_list_length_eager_fallback(input_handle: Any, name: Any, ctx: Any): ...

_TensorListPopBackOutput = namedtuple('TensorListPopBack', ['output_handle', 'tensor'])

def tensor_list_pop_back(input_handle: Any, element_shape: Any, element_dtype: Any, name: Optional[Any] = ...): ...

TensorListPopBack: Any

def tensor_list_pop_back_eager_fallback(input_handle: Any, element_shape: Any, element_dtype: Any, name: Any, ctx: Any): ...
def tensor_list_push_back(input_handle: Any, tensor: Any, name: Optional[Any] = ...): ...

TensorListPushBack: Any

def tensor_list_push_back_eager_fallback(input_handle: Any, tensor: Any, name: Any, ctx: Any): ...
def tensor_list_push_back_batch(input_handles: Any, tensor: Any, name: Optional[Any] = ...): ...

TensorListPushBackBatch: Any

def tensor_list_push_back_batch_eager_fallback(input_handles: Any, tensor: Any, name: Any, ctx: Any): ...
def tensor_list_reserve(element_shape: Any, num_elements: Any, element_dtype: Any, name: Optional[Any] = ...): ...

TensorListReserve: Any

def tensor_list_reserve_eager_fallback(element_shape: Any, num_elements: Any, element_dtype: Any, name: Any, ctx: Any): ...
def tensor_list_resize(input_handle: Any, size: Any, name: Optional[Any] = ...): ...

TensorListResize: Any

def tensor_list_resize_eager_fallback(input_handle: Any, size: Any, name: Any, ctx: Any): ...
def tensor_list_scatter(tensor: Any, indices: Any, element_shape: Any, name: Optional[Any] = ...): ...

TensorListScatter: Any

def tensor_list_scatter_eager_fallback(tensor: Any, indices: Any, element_shape: Any, name: Any, ctx: Any): ...
def tensor_list_scatter_into_existing_list(input_handle: Any, tensor: Any, indices: Any, name: Optional[Any] = ...): ...

TensorListScatterIntoExistingList: Any

def tensor_list_scatter_into_existing_list_eager_fallback(input_handle: Any, tensor: Any, indices: Any, name: Any, ctx: Any): ...
def tensor_list_scatter_v2(tensor: Any, indices: Any, element_shape: Any, num_elements: Any, name: Optional[Any] = ...): ...

TensorListScatterV2: Any

def tensor_list_scatter_v2_eager_fallback(tensor: Any, indices: Any, element_shape: Any, num_elements: Any, name: Any, ctx: Any): ...
def tensor_list_set_item(input_handle: Any, index: Any, item: Any, name: Optional[Any] = ...): ...

TensorListSetItem: Any

def tensor_list_set_item_eager_fallback(input_handle: Any, index: Any, item: Any, name: Any, ctx: Any): ...
def tensor_list_split(tensor: Any, element_shape: Any, lengths: Any, name: Optional[Any] = ...): ...

TensorListSplit: Any

def tensor_list_split_eager_fallback(tensor: Any, element_shape: Any, lengths: Any, name: Any, ctx: Any): ...
def tensor_list_stack(input_handle: Any, element_shape: Any, element_dtype: Any, num_elements: int = ..., name: Optional[Any] = ...): ...

TensorListStack: Any

def tensor_list_stack_eager_fallback(input_handle: Any, element_shape: Any, element_dtype: Any, num_elements: Any, name: Any, ctx: Any): ...
