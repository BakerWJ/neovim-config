from tensorflow.python.keras import layers as keras_layers
from tensorflow.python.layers import base as base
from tensorflow.python.ops import init_ops as init_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class Conv1D(keras_layers.Conv1D, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

def conv1d(inputs: Any, filters: Any, kernel_size: Any, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...

class Conv2D(keras_layers.Conv2D, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., dilation_rate: Any = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

def conv2d(inputs: Any, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., dilation_rate: Any = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...

class Conv3D(keras_layers.Conv3D, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., dilation_rate: Any = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

def conv3d(inputs: Any, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., dilation_rate: Any = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...

class SeparableConv1D(keras_layers.SeparableConv1D, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., depth_multiplier: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., depthwise_initializer: Optional[Any] = ..., pointwise_initializer: Optional[Any] = ..., bias_initializer: Any = ..., depthwise_regularizer: Optional[Any] = ..., pointwise_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., depthwise_constraint: Optional[Any] = ..., pointwise_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

class SeparableConv2D(keras_layers.SeparableConv2D, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., dilation_rate: Any = ..., depth_multiplier: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., depthwise_initializer: Optional[Any] = ..., pointwise_initializer: Optional[Any] = ..., bias_initializer: Any = ..., depthwise_regularizer: Optional[Any] = ..., pointwise_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., depthwise_constraint: Optional[Any] = ..., pointwise_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

def separable_conv1d(inputs: Any, filters: Any, kernel_size: Any, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., depth_multiplier: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., depthwise_initializer: Optional[Any] = ..., pointwise_initializer: Optional[Any] = ..., bias_initializer: Any = ..., depthwise_regularizer: Optional[Any] = ..., pointwise_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., depthwise_constraint: Optional[Any] = ..., pointwise_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...
def separable_conv2d(inputs: Any, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., dilation_rate: Any = ..., depth_multiplier: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., depthwise_initializer: Optional[Any] = ..., pointwise_initializer: Optional[Any] = ..., bias_initializer: Any = ..., depthwise_regularizer: Optional[Any] = ..., pointwise_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., depthwise_constraint: Optional[Any] = ..., pointwise_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...

class Conv2DTranspose(keras_layers.Conv2DTranspose, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

def conv2d_transpose(inputs: Any, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...

class Conv3DTranspose(keras_layers.Conv3DTranspose, base.Layer):
    def __init__(self, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

def conv3d_transpose(inputs: Any, filters: Any, kernel_size: Any, strides: Any = ..., padding: str = ..., data_format: str = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: Optional[Any] = ..., bias_initializer: Any = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., activity_regularizer: Optional[Any] = ..., kernel_constraint: Optional[Any] = ..., bias_constraint: Optional[Any] = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ...): ...
Convolution1D = Conv1D
Convolution2D = Conv2D
Convolution3D = Conv3D
SeparableConvolution2D = SeparableConv2D
Convolution2DTranspose = Conv2DTranspose
Deconvolution2D = Conv2DTranspose
Deconv2D = Conv2DTranspose
Convolution3DTranspose = Conv3DTranspose
Deconvolution3D = Conv3DTranspose
Deconv3D = Conv3DTranspose
convolution1d = conv1d
convolution2d = conv2d
convolution3d = conv3d
separable_convolution2d = separable_conv2d
convolution2d_transpose = conv2d_transpose
deconvolution2d = conv2d_transpose
deconv2d = conv2d_transpose
convolution3d_transpose = conv3d_transpose
deconvolution3d = conv3d_transpose
deconv3d = conv3d_transpose
