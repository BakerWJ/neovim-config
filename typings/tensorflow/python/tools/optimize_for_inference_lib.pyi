from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, graph_pb2 as graph_pb2, node_def_pb2 as node_def_pb2
from tensorflow.python.framework import dtypes as dtypes, graph_util as graph_util, tensor_util as tensor_util
from tensorflow.python.platform import flags as flags_lib, tf_logging as tf_logging
from tensorflow.python.tools import strip_unused_lib as strip_unused_lib
from typing import Any

flags = flags_lib
FLAGS: Any
INPUT_ORDER: Any
EPSILON_ATTR: Any

def optimize_for_inference(input_graph_def: Any, input_node_names: Any, output_node_names: Any, placeholder_type_enum: Any, toco_compatible: bool = ...): ...
def ensure_graph_is_valid(graph_def: Any) -> None: ...
def node_name_from_input(node_name: Any): ...
def node_from_map(node_map: Any, name: Any): ...
def values_from_const(node_def: Any): ...
def scale_after_normalization(node: Any): ...
def fold_batch_norms(input_graph_def: Any): ...
def fuse_resize_and_conv(input_graph_def: Any, output_node_names: Any): ...
