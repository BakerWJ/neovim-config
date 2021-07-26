from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, graph_pb2 as graph_pb2, node_def_pb2 as node_def_pb2
from tensorflow.python.framework import graph_util as graph_util
from tensorflow.python.platform import gfile as gfile
from typing import Any

def strip_unused(input_graph_def: Any, input_node_names: Any, output_node_names: Any, placeholder_type_enum: Any): ...
def strip_unused_from_files(input_graph: Any, input_binary: Any, output_graph: Any, output_binary: Any, input_node_names: Any, output_node_names: Any, placeholder_type_enum: Any): ...
