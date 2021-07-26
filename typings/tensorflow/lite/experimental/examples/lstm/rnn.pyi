from tensorflow.lite.python.op_hint import OpHint as OpHint
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, math_ops as math_ops, rnn_cell_impl as rnn_cell_impl
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def dynamic_rnn(cell: Any, inputs: Any, sequence_length: Optional[Any] = ..., initial_state: Optional[Any] = ..., dtype: Optional[Any] = ..., parallel_iterations: Optional[Any] = ..., swap_memory: bool = ..., time_major: bool = ..., scope: Optional[Any] = ...): ...
def bidirectional_dynamic_rnn(cell_fw: Any, cell_bw: Any, inputs: Any, sequence_length: Optional[Any] = ..., initial_state_fw: Optional[Any] = ..., initial_state_bw: Optional[Any] = ..., dtype: Optional[Any] = ..., parallel_iterations: Optional[Any] = ..., swap_memory: bool = ..., time_major: bool = ..., scope: Optional[Any] = ...): ...
