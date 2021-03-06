from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import constant_op as constant_op, device as device, dtypes as dtypes, ops as ops
from tensorflow.python.keras import activations as activations
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers import recurrent as recurrent
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_cudnn_rnn_ops as gen_cudnn_rnn_ops, math_ops as math_ops, nn as nn, resource_variable_ops as resource_variable_ops, state_ops as state_ops
from tensorflow.python.platform import build_info as build_info
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class GRUCell(recurrent.GRUCell):
    def __init__(self, units: Any, activation: str = ..., recurrent_activation: str = ..., use_bias: bool = ..., kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., dropout: float = ..., recurrent_dropout: float = ..., implementation: int = ..., reset_after: bool = ..., **kwargs: Any) -> None: ...

class GRU(recurrent.DropoutRNNCellMixin, recurrent.GRU):
    def __init__(self, units: Any, activation: str = ..., recurrent_activation: str = ..., use_bias: bool = ..., kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., dropout: float = ..., recurrent_dropout: float = ..., implementation: int = ..., return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., unroll: bool = ..., time_major: bool = ..., reset_after: bool = ..., **kwargs: Any) -> None: ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any, mask: Optional[Any] = ..., training: Optional[Any] = ..., initial_state: Optional[Any] = ...): ...

def standard_gru(inputs: Any, init_h: Any, kernel: Any, recurrent_kernel: Any, bias: Any, activation: Any, recurrent_activation: Any, mask: Any, time_major: Any, go_backwards: Any, sequence_lengths: Any, zero_output_for_mask: Any): ...
def gpu_gru(inputs: Any, init_h: Any, kernel: Any, recurrent_kernel: Any, bias: Any, mask: Any, time_major: Any, go_backwards: Any, sequence_lengths: Any): ...
def gru_with_backend_selection(inputs: Any, init_h: Any, kernel: Any, recurrent_kernel: Any, bias: Any, mask: Any, time_major: Any, go_backwards: Any, activation: Any, recurrent_activation: Any, sequence_lengths: Any, zero_output_for_mask: Any): ...

class LSTMCell(recurrent.LSTMCell):
    def __init__(self, units: Any, activation: str = ..., recurrent_activation: str = ..., use_bias: bool = ..., kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., unit_forget_bias: bool = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., dropout: float = ..., recurrent_dropout: float = ..., implementation: int = ..., **kwargs: Any) -> None: ...

class LSTM(recurrent.DropoutRNNCellMixin, recurrent.LSTM):
    return_runtime: Any = ...
    state_spec: Any = ...
    def __init__(self, units: Any, activation: str = ..., recurrent_activation: str = ..., use_bias: bool = ..., kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., unit_forget_bias: bool = ..., kernel_regularizer: Optional[Any] = ..., recurrent_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., recurrent_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., dropout: float = ..., recurrent_dropout: float = ..., implementation: int = ..., return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., time_major: bool = ..., unroll: bool = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, mask: Optional[Any] = ..., training: Optional[Any] = ..., initial_state: Optional[Any] = ...): ...

def standard_lstm(inputs: Any, init_h: Any, init_c: Any, kernel: Any, recurrent_kernel: Any, bias: Any, activation: Any, recurrent_activation: Any, mask: Any, time_major: Any, go_backwards: Any, sequence_lengths: Any, zero_output_for_mask: Any): ...
def gpu_lstm(inputs: Any, init_h: Any, init_c: Any, kernel: Any, recurrent_kernel: Any, bias: Any, mask: Any, time_major: Any, go_backwards: Any, sequence_lengths: Any): ...
def lstm_with_backend_selection(inputs: Any, init_h: Any, init_c: Any, kernel: Any, recurrent_kernel: Any, bias: Any, mask: Any, time_major: Any, go_backwards: Any, activation: Any, recurrent_activation: Any, sequence_lengths: Any, zero_output_for_mask: Any): ...
def is_sequence_right_padded(mask: Any, time_major: Any): ...
def calculate_sequence_by_mask(mask: Any, time_major: Any): ...
