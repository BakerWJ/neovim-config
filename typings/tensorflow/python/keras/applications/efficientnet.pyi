from tensorflow.python.keras import backend as backend, layers as layers
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

BASE_WEIGHTS_PATH: str
WEIGHTS_HASHES: Any
DEFAULT_BLOCKS_ARGS: Any
CONV_KERNEL_INITIALIZER: Any
DENSE_KERNEL_INITIALIZER: Any

def EfficientNet(width_coefficient: Any, depth_coefficient: Any, default_size: Any, dropout_rate: float = ..., drop_connect_rate: float = ..., depth_divisor: int = ..., activation: str = ..., blocks_args: str = ..., model_name: str = ..., include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., classifier_activation: str = ...): ...
def block(inputs: Any, activation: str = ..., drop_rate: float = ..., name: str = ..., filters_in: int = ..., filters_out: int = ..., kernel_size: int = ..., strides: int = ..., expand_ratio: int = ..., se_ratio: float = ..., id_skip: bool = ...): ...
def EfficientNetB0(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB1(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB2(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB3(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB4(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB5(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB6(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def EfficientNetB7(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., **kwargs: Any): ...
def preprocess_input(x: Any, data_format: Optional[Any] = ...): ...
def decode_predictions(preds: Any, top: int = ...): ...