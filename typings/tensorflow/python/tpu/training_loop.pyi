from tensorflow.python.compiler.xla import xla as xla
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.tpu import tensor_tracer as tensor_tracer, tpu_function as tpu_function
from typing import Any, Optional

def while_loop(condition: Any, body: Any, inputs: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., name: Optional[Any] = ...): ...
def repeat(n: Any, body: Any, inputs: Optional[Any] = ..., infeed_queue: Optional[Any] = ..., name: Optional[Any] = ...): ...
