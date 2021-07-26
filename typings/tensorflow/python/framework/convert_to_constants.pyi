from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, graph_pb2 as graph_pb2, tensor_shape_pb2 as tensor_shape_pb2, variable_pb2 as variable_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.eager import wrap_function as wrap_function
from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.training.saver import export_meta_graph as export_meta_graph
from tensorflow.python.util import object_identity as object_identity
from typing import Any

def disable_lower_using_switch_merge(graph_def: Any): ...
def convert_variables_to_constants_v2(func: Any, lower_control_flow: bool = ..., aggressive_inlining: bool = ...): ...
def convert_variables_to_constants_v2_as_graph(func: Any, lower_control_flow: bool = ..., aggressive_inlining: bool = ...): ...
