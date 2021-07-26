from tensorflow.core.debug import debug_service_pb2 as debug_service_pb2
from tensorflow.core.protobuf import debug_pb2 as debug_pb2
from tensorflow.python.debug.lib import common as common, debug_service_pb2_grpc as debug_service_pb2_grpc, source_utils as source_utils
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.profiler import tfprof_logger as tfprof_logger
from typing import Any

def send_graph_tracebacks(destinations: Any, run_key: Any, origin_stack: Any, graph: Any, send_source: bool = ...) -> None: ...
def send_eager_tracebacks(destinations: Any, origin_stack: Any, send_source: bool = ...) -> None: ...
