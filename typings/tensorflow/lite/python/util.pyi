from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2
from tensorflow.lite.python.op_hint import convert_op_hints_to_stubs as convert_op_hints_to_stubs, find_all_hinted_output_nodes as find_all_hinted_output_nodes
from tensorflow.python.eager import function as function
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from typing import Any, Optional

def convert_dtype_to_tflite_type(tf_dtype: Any): ...
def get_tensor_name(tensor: Any): ...
def get_tensors_from_tensor_names(graph: Any, tensor_names: Any): ...
def set_tensor_shapes(tensors: Any, shapes: Any) -> None: ...
def get_grappler_config(optimizers_list: Any): ...
def run_graph_optimizations(graph_def: Any, input_arrays: Any, output_arrays: Any, config: Any, graph: Optional[Any] = ...): ...
def freeze_graph(sess: Any, input_tensors: Any, output_tensors: Any): ...
def is_frozen_graph(sess: Any): ...
def build_debug_info_func(original_graph: Any): ...
def convert_debug_info_func(saved_debug_info: Any): ...
def get_debug_info(nodes_to_debug_info_func: Any, converted_graph: Any): ...
def convert_bytes_to_c_source(data: Any, array_name: Any, max_line_width: int = ..., include_guard: Optional[Any] = ..., include_path: Optional[Any] = ..., use_tensorflow_license: bool = ...): ...
