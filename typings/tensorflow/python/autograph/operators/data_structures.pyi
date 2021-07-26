from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, list_ops as list_ops, tensor_array_ops as tensor_array_ops
from typing import Any, Optional

def new_list(iterable: Optional[Any] = ...): ...
def tf_tensor_array_new(elements: Any, element_dtype: Optional[Any] = ..., element_shape: Optional[Any] = ...): ...
def tf_tensor_list_new(elements: Any, element_dtype: Optional[Any] = ..., element_shape: Optional[Any] = ...): ...
def list_append(list_: Any, x: Any): ...

class ListPopOpts: ...

def list_pop(list_: Any, i: Any, opts: Any): ...

class ListStackOpts: ...

def list_stack(list_: Any, opts: Any): ...
