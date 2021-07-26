from collections import namedtuple
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.util import tf_should_use as tf_should_use
from typing import Any, Optional

_Resource = namedtuple('_Resource', ['handle', 'create', 'is_initialized'])

def register_resource(handle: Any, create_op: Any, is_initialized_op: Any, is_shared: bool = ...) -> None: ...
def shared_resources(): ...
def local_resources(): ...
def report_uninitialized_resources(resource_list: Optional[Any] = ..., name: str = ...): ...
def initialize_resources(resource_list: Any, name: str = ...): ...
