from tensorflow.python.framework import dtypes as dtypes, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import tensor_array_ops as tensor_array_ops
from typing import Any

def is_dense_tensor(t: Any): ...
def is_tensor_array(t: Any): ...
def is_tensor_list(t: Any): ...
def is_range_tensor(t: Any): ...
