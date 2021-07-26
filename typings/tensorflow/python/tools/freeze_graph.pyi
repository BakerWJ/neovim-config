from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import saver_pb2 as saver_pb2
from tensorflow.core.protobuf.meta_graph_pb2 import MetaGraphDef as MetaGraphDef
from tensorflow.python.client import session as session
from tensorflow.python.framework import graph_util as graph_util, importer as importer
from tensorflow.python.platform import app as app, gfile as gfile
from tensorflow.python.saved_model import loader as loader, tag_constants as tag_constants
from tensorflow.python.tools import saved_model_utils as saved_model_utils
from tensorflow.python.training import checkpoint_management as checkpoint_management, py_checkpoint_reader as py_checkpoint_reader
from typing import Any, Optional

def freeze_graph_with_def_protos(input_graph_def: Any, input_saver_def: Any, input_checkpoint: Any, output_node_names: Any, restore_op_name: Any, filename_tensor_name: Any, output_graph: Any, clear_devices: Any, initializer_nodes: Any, variable_names_whitelist: str = ..., variable_names_blacklist: str = ..., input_meta_graph_def: Optional[Any] = ..., input_saved_model_dir: Optional[Any] = ..., saved_model_tags: Optional[Any] = ..., checkpoint_version: Any = ...): ...
def freeze_graph(input_graph: Any, input_saver: Any, input_binary: Any, input_checkpoint: Any, output_node_names: Any, restore_op_name: Any, filename_tensor_name: Any, output_graph: Any, clear_devices: Any, initializer_nodes: Any, variable_names_whitelist: str = ..., variable_names_blacklist: str = ..., input_meta_graph: Optional[Any] = ..., input_saved_model_dir: Optional[Any] = ..., saved_model_tags: Any = ..., checkpoint_version: Any = ...): ...
def main(unused_args: Any, flags: Any) -> None: ...
def run_main(): ...
