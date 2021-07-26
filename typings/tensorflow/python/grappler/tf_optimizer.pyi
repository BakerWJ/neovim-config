from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2
from typing import Any, Optional

def OptimizeGraph(config_proto: Any, metagraph: Any, verbose: bool = ..., graph_id: bytes = ..., cluster: Optional[Any] = ..., strip_default_attributes: bool = ...): ...
