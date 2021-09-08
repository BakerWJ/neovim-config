from tensorflow.core.protobuf import saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import compat as compat, nest as nest
from typing import Any

def serialize_concrete_function(concrete_function: Any, node_ids: Any, coder: Any): ...
def serialize_bare_concrete_function(concrete_function: Any, name_map: Any): ...
def serialize_function(function: Any, name_map: Any): ...
def wrap_cached_variables(concrete_function: Any): ...