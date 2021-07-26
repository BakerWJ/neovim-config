from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2
from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, custom_gradient as custom_gradient, lookup_ops as lookup_ops, resource_variable_ops as resource_variable_ops, variables as variables
from tensorflow.python.saved_model import function_deserialization as function_deserialization, load_v1_in_v2 as load_v1_in_v2, loader_impl as loader_impl, nested_structure_coder as nested_structure_coder, revived_types as revived_types
from tensorflow.python.training.tracking import base as base, graph_view as graph_view, tracking as tracking, util as util
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _WrapperFunction(function.ConcreteFunction):
    def __init__(self, concrete_function: Any) -> None: ...

class Loader:
    def __init__(self, object_graph_proto: Any, saved_model_proto: Any, export_dir: Any) -> None: ...
    def adjust_debug_info_func_names(self, debug_info: Any): ...
    def get(self, node_id: Any): ...

class _RestoredResource(tracking.TrackableResource):
    def __init__(self, device: str = ...) -> None: ...

def load(export_dir: Any, tags: Optional[Any] = ...): ...
def load_internal(export_dir: Any, tags: Optional[Any] = ..., loader_cls: Any = ...): ...
