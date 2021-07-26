from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def audio_spectrogram(input: Any, window_size: Any, stride: Any, magnitude_squared: bool = ..., name: Optional[Any] = ...): ...

AudioSpectrogram: Any

def audio_spectrogram_eager_fallback(input: Any, window_size: Any, stride: Any, magnitude_squared: Any, name: Any, ctx: Any): ...

_DecodeWavOutput = namedtuple('DecodeWav', ['audio', 'sample_rate'])

def decode_wav(contents: Any, desired_channels: int = ..., desired_samples: int = ..., name: Optional[Any] = ...): ...

DecodeWav: Any

def decode_wav_eager_fallback(contents: Any, desired_channels: Any, desired_samples: Any, name: Any, ctx: Any): ...
def encode_wav(audio: Any, sample_rate: Any, name: Optional[Any] = ...): ...

EncodeWav: Any

def encode_wav_eager_fallback(audio: Any, sample_rate: Any, name: Any, ctx: Any): ...
def mfcc(spectrogram: Any, sample_rate: Any, upper_frequency_limit: int = ..., lower_frequency_limit: int = ..., filterbank_channel_count: int = ..., dct_coefficient_count: int = ..., name: Optional[Any] = ...): ...

Mfcc: Any

def mfcc_eager_fallback(spectrogram: Any, sample_rate: Any, upper_frequency_limit: Any, lower_frequency_limit: Any, filterbank_channel_count: Any, dct_coefficient_count: Any, name: Any, ctx: Any): ...
