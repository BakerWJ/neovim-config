from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any

def sequence_length_from_sparse_tensor(sp_tensor: Any, num_elements: int = ...): ...
def assert_string_or_int(dtype: Any, prefix: Any) -> None: ...
def assert_key_is_string(key: Any) -> None: ...
def check_default_value(shape: Any, default_value: Any, dtype: Any, key: Any): ...
