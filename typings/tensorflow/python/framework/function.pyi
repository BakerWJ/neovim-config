from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, function_pb2 as function_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import c_api_util as c_api_util, dtypes as dtypes, graph_to_function_def as graph_to_function_def, ops as ops
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, function_utils as function_utils, tf_contextlib as tf_contextlib, tf_inspect as tf_inspect
from typing import Any, Optional

class Defun:
    def __init__(self, *input_types: Any, **kwargs: Any) -> None: ...
    def __call__(self, func: Any): ...

class _DefinedFunctionDeleter:
    name: Any = ...
    def __init__(self, name: Any) -> None: ...
    def __del__(self) -> None: ...

class _DefinedFunction:
    def __init__(self, func: Any, argnames: Any, input_types: Any, func_name: Optional[Any] = ..., grad_func: Optional[Any] = ..., python_grad_func: Optional[Any] = ..., out_names: Optional[Any] = ..., shape_func: Optional[Any] = ..., capture_by_value: bool = ..., whitelisted_stateful_ops: Optional[Any] = ..., capture_resource_var_by_value: bool = ..., **kwargs: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def definition(self): ...
    def set_grad_func(self, grad_func: Any) -> None: ...
    @property
    def grad_func_name(self): ...
    @property
    def python_grad_func(self): ...
    @property
    def declared_input_types(self): ...
    @property
    def captured_inputs(self): ...
    @property
    def stateful_ops(self): ...
    def add_to_graph(self, g: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...

class _OverloadedFunction:
    def __init__(self, func: Any, argnames: Any, func_name: Optional[Any] = ..., grad_func: Optional[Any] = ..., python_grad_func: Optional[Any] = ..., out_names: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def instantiate(self, input_types: Any): ...
    def __call__(self, *args: Any, **kwargs: Any): ...

class _FuncGraph(ops.Graph):
    name: Any = ...
    inputs: Any = ...
    outputs: Any = ...
    extra_inputs: Any = ...
    extra_args: Any = ...
    extra_vars: Any = ...
    def __init__(self, name: Any, capture_by_value: Any, whitelisted_stateful_ops: Any, capture_resource_var_by_value: Any, *args: Any, **kwargs: Any) -> None: ...
    @property
    def outer_graph(self): ...
    def container(self, container_name: Any) -> None: ...
    def getvar(self, getter: Any, name: Any, shape: Optional[Any] = ..., dtype: Optional[Any] = ..., initializer: Optional[Any] = ..., reuse: Optional[Any] = ..., trainable: bool = ..., collections: Optional[Any] = ..., use_resource: Optional[Any] = ..., **kwargs: Any): ...
    def capture(self, tensor: Any, name: Optional[Any] = ...): ...
    @property
    def captures(self): ...

def func_graph_from_py_func(func: Any, arg_names: Any, arg_types: Any, name: Optional[Any] = ..., capture_by_value: bool = ..., device: Optional[Any] = ..., colocation_stack: Optional[Any] = ..., container: Optional[Any] = ..., collections_ref: Optional[Any] = ..., arg_shapes: Optional[Any] = ..., whitelisted_stateful_ops: Optional[Any] = ..., capture_resource_var_by_value: bool = ...): ...
def from_library(lib: Any): ...
def get_extra_vars(): ...
def get_extra_inputs(): ...
def get_extra_args(): ...
def function_def_from_tf_function(c_func: Any): ...