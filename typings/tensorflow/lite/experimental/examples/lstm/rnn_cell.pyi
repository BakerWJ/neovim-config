from tensorflow.lite.python.op_hint import OpHint as OpHint
from tensorflow.python.keras import activations as activations, initializers as initializers
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, init_ops as init_ops, math_ops as math_ops, nn_ops as nn_ops, partitioned_variables as partitioned_variables, rnn_cell_impl as rnn_cell_impl
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class TfLiteRNNCell(rnn_cell_impl.LayerRNNCell):
    input_spec: Any = ...
    def __init__(self, num_units: Any, activation: Optional[Any] = ..., reuse: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool = ...
    def build(self, inputs_shape: Any): ...
    def call(self, inputs: Any, state: Any): ...
    def get_config(self): ...

class TFLiteLSTMCell(rnn_cell_impl.LayerRNNCell):
    input_spec: Any = ...
    def __init__(self, num_units: Any, use_peepholes: bool = ..., cell_clip: Optional[Any] = ..., initializer: Optional[Any] = ..., num_proj: Optional[Any] = ..., proj_clip: Optional[Any] = ..., num_unit_shards: Optional[Any] = ..., num_proj_shards: Optional[Any] = ..., forget_bias: float = ..., state_is_tuple: bool = ..., activation: Optional[Any] = ..., reuse: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    input_to_input_w: Any = ...
    input_to_forget_w: Any = ...
    input_to_cell_w: Any = ...
    input_to_output_w: Any = ...
    cell_to_input_w: Any = ...
    cell_to_forget_w: Any = ...
    cell_to_cell_w: Any = ...
    cell_to_output_w: Any = ...
    input_bias: Any = ...
    forget_bias: Any = ...
    cell_bias: Any = ...
    output_bias: Any = ...
    built: bool = ...
    def build(self, inputs_shape: Any): ...
    def call(self, inputs: Any, state: Any): ...
    def get_config(self): ...
