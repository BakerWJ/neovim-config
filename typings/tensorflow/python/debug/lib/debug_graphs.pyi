from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python.framework import op_def_registry as op_def_registry
from typing import Any, Optional

def parse_node_or_tensor_name(name: Any): ...
def get_node_name(element_name: Any): ...
def get_output_slot(element_name: Any): ...
def is_copy_node(node_name: Any): ...
def is_debug_node(node_name: Any): ...
def parse_debug_node_name(node_name: Any): ...

class GraphTracingReachedDestination(Exception): ...

class DFSGraphTracer:
    def __init__(self, input_lists: Any, skip_node_names: Optional[Any] = ..., destination_node_name: Optional[Any] = ...) -> None: ...
    def trace(self, graph_element_name: Any) -> None: ...
    def inputs(self): ...
    def depth_list(self): ...

class DebugGraph:
    def __init__(self, debug_graph_def: Any, device_name: Optional[Any] = ...) -> None: ...
    @property
    def device_name(self): ...
    @property
    def debug_graph_def(self): ...
    @property
    def non_debug_graph_def(self): ...
    @property
    def node_devices(self): ...
    @property
    def node_op_types(self): ...
    @property
    def node_attributes(self): ...
    @property
    def node_inputs(self): ...
    @property
    def node_ctrl_inputs(self): ...
    @property
    def node_reversed_ref_inputs(self): ...
    @property
    def node_recipients(self): ...
    @property
    def node_ctrl_recipients(self): ...

def reconstruct_non_debug_graph_def(debug_graph_def: Any): ...
