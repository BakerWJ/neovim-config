from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2
from tensorflow.python.client import session as session
from tensorflow.python.framework import graph_util as graph_util, tensor_shape as tensor_shape, versions as versions
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.platform import test as test
from typing import Any

def aot_compile_cpu_meta_graph_def(checkpoint_path: Any, meta_graph_def: Any, output_prefix: Any, signature_def_key: Any, cpp_class: Any, target_triple: Any, variables_to_feed: Any = ..., enable_multithreading: bool = ...) -> None: ...
