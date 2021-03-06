from tensorflow.python.autograph.utils import py_func as py_func, tensors as tensors
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_parsing_ops as gen_parsing_ops, gen_string_ops as gen_string_ops, list_ops as list_ops, math_ops as math_ops, sort_ops as sort_ops
from tensorflow.python.util import lazy_loader as lazy_loader, nest as nest
from typing import Any

input_lib: Any
parallel_ops: Any
UNSPECIFIED: Any

def overload_of(f: Any): ...
def eval_in_original_context(f: Any, args: Any, caller_fn_scope: Any): ...
def super_in_original_context(f: Any, args: Any, caller_fn_scope: Any): ...
def abs_(x: Any): ...
def float_(x: int = ...): ...
def int_(x: int = ..., base: Any = ...): ...
def len_(s: Any): ...
def print_(*objects: Any, **kwargs: Any): ...
def range_(start_or_stop: Any, stop: Any = ..., step: Any = ...): ...
def enumerate_(s: Any, start: int = ...): ...
def zip_(*iterables: Any): ...
def map_(fn: Any, *iterables: Any): ...
def filter_(function: Any, iterable: Any): ...
def any_(iterable: Any): ...
def all_(iterable: Any): ...
def sorted_(iterable: Any, key: Any = ..., reverse: Any = ...): ...

SUPPORTED_BUILTINS: Any
BUILTIN_FUNCTIONS_MAP: Any
