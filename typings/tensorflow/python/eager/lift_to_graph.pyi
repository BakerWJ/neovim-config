from collections import namedtuple
from tensorflow.python.framework import func_graph as func_graph, ops as ops
from tensorflow.python.ops import array_ops as array_ops, op_selector as op_selector, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, object_identity as object_identity
from typing import Any, Optional

UnliftableError = op_selector.UnliftableError

_InputMutation = namedtuple('_InputMutation', ['copied_op', 'input_index', 'old_graph_tensor'])

_ControlMutation = namedtuple('_ControlMutation', ['copied_op', 'old_graph_op'])

def lift_to_graph(tensors: Any, graph: Any, sources: Optional[Any] = ..., disallowed_placeholders: Optional[Any] = ..., add_sources: bool = ..., handle_captures: bool = ..., base_graph: Optional[Any] = ..., op_map: Optional[Any] = ...): ...
