from tensorflow.core.debug import debug_service_pb2 as debug_service_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.client import session as session
from tensorflow.python.debug.lib import debug_data as debug_data, debug_utils as debug_utils, grpc_debug_server as grpc_debug_server
from tensorflow.python.framework import constant_op as constant_op, errors as errors
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.util import compat as compat
from typing import Any, Optional

class EventListenerTestStreamHandler(grpc_debug_server.EventListenerBaseStreamHandler):
    def __init__(self, dump_dir: Any, event_listener_servicer: Any) -> None: ...
    def on_core_metadata_event(self, event: Any) -> None: ...
    def on_graph_def(self, graph_def: Any, device_name: Any, wall_time: Any) -> None: ...
    def on_value_event(self, event: Any): ...

class EventListenerTestServicer(grpc_debug_server.EventListenerBaseServicer):
    core_metadata_json_strings: Any = ...
    partition_graph_defs: Any = ...
    debug_tensor_values: Any = ...
    def __init__(self, server_port: Any, dump_dir: Any, toggle_watch_on_core_metadata: Optional[Any] = ...) -> None: ...
    def toggle_watch(self) -> None: ...
    def clear_data(self) -> None: ...
    def SendTracebacks(self, request: Any, context: Any): ...
    def SendSourceFiles(self, request: Any, context: Any): ...
    def query_op_traceback(self, op_name: Any): ...
    def query_origin_stack(self): ...
    def query_call_types(self): ...
    def query_call_keys(self): ...
    def query_graph_versions(self): ...
    def query_source_file_line(self, file_path: Any, lineno: Any): ...

def start_server_on_separate_thread(dump_to_filesystem: bool = ..., server_start_delay_sec: float = ..., poll_server: bool = ..., blocking: bool = ..., toggle_watch_on_core_metadata: Optional[Any] = ...): ...
