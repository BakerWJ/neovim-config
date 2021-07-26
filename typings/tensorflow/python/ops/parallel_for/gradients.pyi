from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops
from tensorflow.python.ops.parallel_for import control_flow_ops as control_flow_ops
from tensorflow.python.util import nest as nest
from typing import Any, Optional

def jacobian(output: Any, inputs: Any, use_pfor: bool = ..., parallel_iterations: Optional[Any] = ...): ...
def batch_jacobian(output: Any, inp: Any, use_pfor: bool = ..., parallel_iterations: Optional[Any] = ...): ...
