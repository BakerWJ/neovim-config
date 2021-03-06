from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import context as context, lift_to_graph as lift_to_graph
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import nest as nest, object_identity as object_identity, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

FREQUENT_TRACING_WARNING_MAX_CALL_HISTORY: int
FREQUENT_TRACING_WARNING_THRESHOLD: int

class _CallCounter:
    call_count: int = ...
    def __init__(self, max_call_history: Any) -> None: ...
    def called_with_tracing(self) -> None: ...
    def called_without_tracing(self) -> None: ...
    def get_tracing_count(self): ...

class UnliftedInitializerVariable(resource_variable_ops.UninitializedVariable):
    def __init__(self, initial_value: Optional[Any] = ..., trainable: Optional[Any] = ..., caching_device: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., constraint: Optional[Any] = ..., add_initializers_to: Optional[Any] = ..., lifted_initializer_graph: Optional[Any] = ..., synchronization: Optional[Any] = ..., aggregation: Optional[Any] = ..., shape: Optional[Any] = ..., **unused_kwargs: Any): ...

RUN_FUNCTIONS_EAGERLY: bool

def run_functions_eagerly(run_eagerly: Any) -> None: ...
def functions_run_eagerly(): ...

class FunctionDeleter:
    func_graph: Any = ...
    def __init__(self, func_graph: Any) -> None: ...
    def __del__(self) -> None: ...

class Function:
    def __init__(self, python_function: Any, name: Any, input_signature: Optional[Any] = ..., autograph: bool = ..., experimental_implements: Optional[Any] = ..., experimental_autograph_options: Optional[Any] = ..., experimental_relax_shapes: bool = ..., experimental_compile: Optional[Any] = ...) -> None: ...
    def __call__(self, *args: Any, **kwds: Any): ...
    @property
    def python_function(self): ...
    @property
    def input_signature(self): ...
    @property
    def function_spec(self): ...
    def get_initialization_function(self, *args: Any, **kwargs: Any): ...
    def get_concrete_function(self, *args: Any, **kwargs: Any): ...
    def __get__(self, instance: Any, owner: Any): ...

def function(func: Optional[Any] = ..., input_signature: Optional[Any] = ..., autograph: bool = ..., experimental_implements: Optional[Any] = ..., experimental_autograph_options: Optional[Any] = ..., experimental_relax_shapes: bool = ..., experimental_compile: Optional[Any] = ...): ...
