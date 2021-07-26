from tensorflow.python.ops import gen_spectral_ops as gen_spectral_ops, manip_ops as manip_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

fft: Any
ifft: Any
fft2d: Any
ifft2d: Any
fft3d: Any
ifft3d: Any
rfft: Any
irfft: Any
rfft2d: Any
irfft2d: Any
rfft3d: Any
irfft3d: Any

def fftshift(x: Any, axes: Optional[Any] = ..., name: Optional[Any] = ...): ...
def ifftshift(x: Any, axes: Optional[Any] = ..., name: Optional[Any] = ...): ...
