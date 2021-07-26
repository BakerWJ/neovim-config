from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import function_def_to_graph as function_def_to_graph, ops as ops
from tensorflow.python.framework.func_graph import FuncGraph as FuncGraph
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.ops import control_flow_util as control_flow_util, control_flow_v2_func_graphs as control_flow_v2_func_graphs
from tensorflow.python.util import tf_contextlib as tf_contextlib
from typing import Any

CondBranchFuncGraph = control_flow_v2_func_graphs.CondBranchFuncGraph
WhileCondFuncGraph = control_flow_v2_func_graphs.WhileCondFuncGraph
WhileBodyFuncGraph = control_flow_v2_func_graphs.WhileBodyFuncGraph

def in_defun(): ...
def create_new_tf_function(func_graph: Any): ...
def unique_fn_name(scope: Any, name: Any): ...
def unique_grad_fn_name(forward_name: Any): ...
def maybe_set_lowering_attr(op: Any) -> None: ...
def maybe_propagate_compile_time_consts_in_xla(op: Any) -> None: ...
def resource_input_index(tensor_name: Any, input_names: Any, node_defs: Any, functions: Any): ...
def clear_control_inputs() -> None: ...
def output_all_intermediates(): ...
def get_func_graph(op: Any, input_shapes: Any, func_name: Any): ...
