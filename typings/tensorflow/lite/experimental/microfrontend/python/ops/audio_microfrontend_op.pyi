from tensorflow.lite.experimental.microfrontend.ops import gen_audio_microfrontend_op as gen_audio_microfrontend_op
from tensorflow.python.framework import dtypes as dtypes, load_library as load_library, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.platform import resource_loader as resource_loader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def audio_microfrontend(audio: Any, sample_rate: int = ..., window_size: int = ..., window_step: int = ..., num_channels: int = ..., upper_band_limit: float = ..., lower_band_limit: float = ..., smoothing_bits: int = ..., even_smoothing: float = ..., odd_smoothing: float = ..., min_signal_remaining: float = ..., enable_pcan: bool = ..., pcan_strength: float = ..., pcan_offset: float = ..., gain_bits: int = ..., enable_log: bool = ..., scale_shift: int = ..., left_context: int = ..., right_context: int = ..., frame_stride: int = ..., zero_padding: bool = ..., out_scale: int = ..., out_type: Any = ...): ...
