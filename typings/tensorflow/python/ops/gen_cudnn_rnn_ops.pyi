from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_CudnnRNNOutput = namedtuple('CudnnRNN', ['output', 'output_h', 'output_c', 'reserve_space'])

def cudnn_rnn(input: Any, input_h: Any, input_c: Any, params: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., is_training: bool = ..., name: Optional[Any] = ...): ...

CudnnRNN: Any

def cudnn_rnn_eager_fallback(input: Any, input_h: Any, input_c: Any, params: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, is_training: Any, name: Any, ctx: Any): ...

_CudnnRNNBackpropOutput = namedtuple('CudnnRNNBackprop', ['input_backprop', 'input_h_backprop', 'input_c_backprop', 'params_backprop'])

def cudnn_rnn_backprop(input: Any, input_h: Any, input_c: Any, params: Any, output: Any, output_h: Any, output_c: Any, output_backprop: Any, output_h_backprop: Any, output_c_backprop: Any, reserve_space: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

CudnnRNNBackprop: Any

def cudnn_rnn_backprop_eager_fallback(input: Any, input_h: Any, input_c: Any, params: Any, output: Any, output_h: Any, output_c: Any, output_backprop: Any, output_h_backprop: Any, output_c_backprop: Any, reserve_space: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_CudnnRNNBackpropV2Output = namedtuple('CudnnRNNBackpropV2', ['input_backprop', 'input_h_backprop', 'input_c_backprop', 'params_backprop'])

def cudnn_rnn_backprop_v2(input: Any, input_h: Any, input_c: Any, params: Any, output: Any, output_h: Any, output_c: Any, output_backprop: Any, output_h_backprop: Any, output_c_backprop: Any, reserve_space: Any, host_reserved: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

CudnnRNNBackpropV2: Any

def cudnn_rnn_backprop_v2_eager_fallback(input: Any, input_h: Any, input_c: Any, params: Any, output: Any, output_h: Any, output_c: Any, output_backprop: Any, output_h_backprop: Any, output_c_backprop: Any, reserve_space: Any, host_reserved: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_CudnnRNNBackpropV3Output = namedtuple('CudnnRNNBackpropV3', ['input_backprop', 'input_h_backprop', 'input_c_backprop', 'params_backprop'])

def cudnn_rnn_backprop_v3(input: Any, input_h: Any, input_c: Any, params: Any, sequence_lengths: Any, output: Any, output_h: Any, output_c: Any, output_backprop: Any, output_h_backprop: Any, output_c_backprop: Any, reserve_space: Any, host_reserved: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., time_major: bool = ..., name: Optional[Any] = ...): ...

CudnnRNNBackpropV3: Any

def cudnn_rnn_backprop_v3_eager_fallback(input: Any, input_h: Any, input_c: Any, params: Any, sequence_lengths: Any, output: Any, output_h: Any, output_c: Any, output_backprop: Any, output_h_backprop: Any, output_c_backprop: Any, reserve_space: Any, host_reserved: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, num_proj: Any, time_major: Any, name: Any, ctx: Any): ...
def cudnn_rnn_canonical_to_params(num_layers: Any, num_units: Any, input_size: Any, weights: Any, biases: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

CudnnRNNCanonicalToParams: Any

def cudnn_rnn_canonical_to_params_eager_fallback(num_layers: Any, num_units: Any, input_size: Any, weights: Any, biases: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
def cudnn_rnn_canonical_to_params_v2(num_layers: Any, num_units: Any, input_size: Any, weights: Any, biases: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., name: Optional[Any] = ...): ...

CudnnRNNCanonicalToParamsV2: Any

def cudnn_rnn_canonical_to_params_v2_eager_fallback(num_layers: Any, num_units: Any, input_size: Any, weights: Any, biases: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, num_proj: Any, name: Any, ctx: Any): ...
def cudnn_rnn_params_size(num_layers: Any, num_units: Any, input_size: Any, T: Any, S: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., name: Optional[Any] = ...): ...

CudnnRNNParamsSize: Any

def cudnn_rnn_params_size_eager_fallback(num_layers: Any, num_units: Any, input_size: Any, T: Any, S: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, num_proj: Any, name: Any, ctx: Any): ...

_CudnnRNNParamsToCanonicalOutput = namedtuple('CudnnRNNParamsToCanonical', ['weights', 'biases'])

def cudnn_rnn_params_to_canonical(num_layers: Any, num_units: Any, input_size: Any, params: Any, num_params: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

CudnnRNNParamsToCanonical: Any

def cudnn_rnn_params_to_canonical_eager_fallback(num_layers: Any, num_units: Any, input_size: Any, params: Any, num_params: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_CudnnRNNParamsToCanonicalV2Output = namedtuple('CudnnRNNParamsToCanonicalV2', ['weights', 'biases'])

def cudnn_rnn_params_to_canonical_v2(num_layers: Any, num_units: Any, input_size: Any, params: Any, num_params_weights: Any, num_params_biases: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., name: Optional[Any] = ...): ...

CudnnRNNParamsToCanonicalV2: Any

def cudnn_rnn_params_to_canonical_v2_eager_fallback(num_layers: Any, num_units: Any, input_size: Any, params: Any, num_params_weights: Any, num_params_biases: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, num_proj: Any, name: Any, ctx: Any): ...

_CudnnRNNV2Output = namedtuple('CudnnRNNV2', ['output', 'output_h', 'output_c', 'reserve_space', 'host_reserved'])

def cudnn_rnnv2(input: Any, input_h: Any, input_c: Any, params: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., is_training: bool = ..., name: Optional[Any] = ...): ...

CudnnRNNV2: Any

def cudnn_rnnv2_eager_fallback(input: Any, input_h: Any, input_c: Any, params: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, is_training: Any, name: Any, ctx: Any): ...

_CudnnRNNV3Output = namedtuple('CudnnRNNV3', ['output', 'output_h', 'output_c', 'reserve_space', 'host_reserved'])

def cudnn_rnnv3(input: Any, input_h: Any, input_c: Any, params: Any, sequence_lengths: Any, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., is_training: bool = ..., time_major: bool = ..., name: Optional[Any] = ...): ...

CudnnRNNV3: Any

def cudnn_rnnv3_eager_fallback(input: Any, input_h: Any, input_c: Any, params: Any, sequence_lengths: Any, rnn_mode: Any, input_mode: Any, direction: Any, dropout: Any, seed: Any, seed2: Any, num_proj: Any, is_training: Any, time_major: Any, name: Any, ctx: Any): ...
