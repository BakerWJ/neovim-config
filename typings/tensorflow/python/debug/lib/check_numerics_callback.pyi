from tensorflow.core.protobuf import debug_event_pb2 as debug_event_pb2
from tensorflow.python.debug.lib import op_callbacks_common as op_callbacks_common, source_utils as source_utils
from tensorflow.python.framework import op_callbacks as op_callbacks, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_debug_ops as gen_debug_ops
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

IGNORE_OP_OUTPUTS: Any
SAFE_OPS: Any

def limit_string_length(string: Any, max_len: int = ...): ...
def get_check_numerics_error_message(slot: Any, num_outputs: Any, op_type: Any, tensor: Any, inputs: Any, graph: Optional[Any] = ..., traceback: Optional[Any] = ..., stack_height_limit: int = ..., path_length_limit: int = ...): ...

class CheckNumericsCallback:
    def __init__(self, stack_height_limit: Any, path_length_limit: Any) -> None: ...
    def callback(self, op_type: Any, inputs: Any, attrs: Any, outputs: Any, op_name: Optional[Any] = ..., graph: Optional[Any] = ...): ...

def enable_check_numerics(stack_height_limit: int = ..., path_length_limit: int = ...) -> None: ...
def disable_check_numerics() -> None: ...
