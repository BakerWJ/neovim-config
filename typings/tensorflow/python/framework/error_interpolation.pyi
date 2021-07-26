from collections import namedtuple
from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2
from typing import Any

_ParseTag = namedtuple('_ParseTag', ['type', 'name'])

def parse_message(message: Any): ...
def create_graph_debug_info_def(func_named_operations: Any): ...
def traceback_files_common_prefix(all_ops: Any): ...
def interpolate(error_message: Any, graph: Any): ...
