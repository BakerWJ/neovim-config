from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from typing import Any, Optional

def alias_inplace_update(x: Any, i: Any, v: Any): ...
def alias_inplace_add(x: Any, i: Any, v: Any): ...
def alias_inplace_sub(x: Any, i: Any, v: Any): ...
def empty_like(x: Any, init: Optional[Any] = ...): ...
def inplace_update(x: Any, i: Any, v: Any): ...
def inplace_add(x: Any, i: Any, v: Any): ...
def inplace_sub(x: Any, i: Any, v: Any): ...

empty: Any
