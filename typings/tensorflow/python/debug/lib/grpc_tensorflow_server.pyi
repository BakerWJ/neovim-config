from tensorflow.core.protobuf import config_pb2 as config_pb2, tensorflow_server_pb2 as tensorflow_server_pb2
from tensorflow.python.platform import app as app
from tensorflow.python.training import server_lib as server_lib
from typing import Any

def parse_cluster_spec(cluster_spec: Any, cluster: Any, verbose: bool = ...) -> None: ...
def main(unused_args: Any) -> None: ...
