from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def audio_microfrontend(audio: Any, sample_rate: int = ..., window_size: int = ..., window_step: int = ..., num_channels: int = ..., upper_band_limit: int = ..., lower_band_limit: int = ..., smoothing_bits: int = ..., even_smoothing: float = ..., odd_smoothing: float = ..., min_signal_remaining: float = ..., enable_pcan: bool = ..., pcan_strength: float = ..., pcan_offset: int = ..., gain_bits: int = ..., enable_log: bool = ..., scale_shift: int = ..., left_context: int = ..., right_context: int = ..., frame_stride: int = ..., zero_padding: bool = ..., out_scale: int = ..., out_type: Any = ..., name: Optional[Any] = ...): ...

AudioMicrofrontend: Any

def audio_microfrontend_eager_fallback(audio: Any, sample_rate: Any, window_size: Any, window_step: Any, num_channels: Any, upper_band_limit: Any, lower_band_limit: Any, smoothing_bits: Any, even_smoothing: Any, odd_smoothing: Any, min_signal_remaining: Any, enable_pcan: Any, pcan_strength: Any, pcan_offset: Any, gain_bits: Any, enable_log: Any, scale_shift: Any, left_context: Any, right_context: Any, frame_stride: Any, zero_padding: Any, out_scale: Any, out_type: Any, name: Any, ctx: Any): ...
