from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import constant_op as constant_op, func_graph as func_graph, function as function, ops as ops
from tensorflow.python.ops import gen_script_ops as gen_script_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation, lazy_loader as lazy_loader, nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

autograph: Any
tape_cache: Any

class EagerFunc:
    def __init__(self, func: Any, Tout: Any, is_grad_func: Any) -> None: ...
    def __call__(self, device: Any, token: Any, args: Any): ...

class FuncRegistry:
    def __init__(self) -> None: ...
    def insert(self, func: Any): ...
    def remove(self, token: Any) -> None: ...
    def __call__(self, token: Any, device: Any, args: Any): ...
    def size(self): ...

def eager_py_func(func: Any, inp: Any, Tout: Any, name: Optional[Any] = ...): ...
def py_func_common(func: Any, inp: Any, Tout: Any, stateful: bool = ..., name: Optional[Any] = ...): ...
def py_func(func: Any, inp: Any, Tout: Any, stateful: bool = ..., name: Optional[Any] = ...): ...
def numpy_function(func: Any, inp: Any, Tout: Any, name: Optional[Any] = ...): ...
