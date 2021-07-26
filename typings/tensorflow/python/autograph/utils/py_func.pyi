from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.ops import script_ops as script_ops
from typing import Any, Optional

class MatchDType: ...

def wrap_py_func(f: Any, return_dtypes: Any, args: Any, kwargs: Optional[Any] = ..., use_dummy_return: bool = ...): ...
