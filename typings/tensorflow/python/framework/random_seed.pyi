from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

DEFAULT_GRAPH_SEED: int

def get_seed(op_seed: Any): ...
def set_random_seed(seed: Any) -> None: ...
def set_seed(seed: Any) -> None: ...
