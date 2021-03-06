from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.utils import conv_utils as conv_utils
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class Pooling1D(Layer):
    pool_function: Any = ...
    pool_size: Any = ...
    strides: Any = ...
    padding: Any = ...
    data_format: Any = ...
    input_spec: Any = ...
    def __init__(self, pool_function: Any, pool_size: Any, strides: Any, padding: str = ..., data_format: str = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class MaxPooling1D(Pooling1D):
    def __init__(self, pool_size: int = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: str = ..., **kwargs: Any) -> None: ...

class AveragePooling1D(Pooling1D):
    def __init__(self, pool_size: int = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: str = ..., **kwargs: Any) -> None: ...

class Pooling2D(Layer):
    pool_function: Any = ...
    pool_size: Any = ...
    strides: Any = ...
    padding: Any = ...
    data_format: Any = ...
    input_spec: Any = ...
    def __init__(self, pool_function: Any, pool_size: Any, strides: Any, padding: str = ..., data_format: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class MaxPooling2D(Pooling2D):
    def __init__(self, pool_size: Any = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., **kwargs: Any) -> None: ...

class AveragePooling2D(Pooling2D):
    def __init__(self, pool_size: Any = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., **kwargs: Any) -> None: ...

class Pooling3D(Layer):
    pool_function: Any = ...
    pool_size: Any = ...
    strides: Any = ...
    padding: Any = ...
    data_format: Any = ...
    input_spec: Any = ...
    def __init__(self, pool_function: Any, pool_size: Any, strides: Any, padding: str = ..., data_format: str = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class MaxPooling3D(Pooling3D):
    def __init__(self, pool_size: Any = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., **kwargs: Any) -> None: ...

class AveragePooling3D(Pooling3D):
    def __init__(self, pool_size: Any = ..., strides: Optional[Any] = ..., padding: str = ..., data_format: Optional[Any] = ..., **kwargs: Any) -> None: ...

class GlobalPooling1D(Layer):
    input_spec: Any = ...
    data_format: Any = ...
    def __init__(self, data_format: str = ..., **kwargs: Any) -> None: ...
    def compute_output_shape(self, input_shape: Any): ...
    def call(self, inputs: Any) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling1D(GlobalPooling1D):
    supports_masking: bool = ...
    def __init__(self, data_format: str = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, mask: Optional[Any] = ...): ...
    def compute_mask(self, inputs: Any, mask: Optional[Any] = ...) -> None: ...

class GlobalMaxPooling1D(GlobalPooling1D):
    def call(self, inputs: Any): ...

class GlobalPooling2D(Layer):
    data_format: Any = ...
    input_spec: Any = ...
    def __init__(self, data_format: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def compute_output_shape(self, input_shape: Any): ...
    def call(self, inputs: Any) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling2D(GlobalPooling2D):
    def call(self, inputs: Any): ...

class GlobalMaxPooling2D(GlobalPooling2D):
    def call(self, inputs: Any): ...

class GlobalPooling3D(Layer):
    data_format: Any = ...
    input_spec: Any = ...
    def __init__(self, data_format: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def compute_output_shape(self, input_shape: Any): ...
    def call(self, inputs: Any) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling3D(GlobalPooling3D):
    def call(self, inputs: Any): ...

class GlobalMaxPooling3D(GlobalPooling3D):
    def call(self, inputs: Any): ...
AvgPool1D = AveragePooling1D
MaxPool1D = MaxPooling1D
AvgPool2D = AveragePooling2D
MaxPool2D = MaxPooling2D
AvgPool3D = AveragePooling3D
MaxPool3D = MaxPooling3D
GlobalMaxPool1D = GlobalMaxPooling1D
GlobalMaxPool2D = GlobalMaxPooling2D
GlobalMaxPool3D = GlobalMaxPooling3D
GlobalAvgPool1D = GlobalAveragePooling1D
GlobalAvgPool2D = GlobalAveragePooling2D
GlobalAvgPool3D = GlobalAveragePooling3D
