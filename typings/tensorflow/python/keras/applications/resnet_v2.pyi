from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils, resnet as resnet
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

def ResNet50V2(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., classifier_activation: str = ...): ...
def ResNet101V2(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., classifier_activation: str = ...): ...
def ResNet152V2(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., classifier_activation: str = ...): ...
def preprocess_input(x: Any, data_format: Optional[Any] = ...): ...
def decode_predictions(preds: Any, top: int = ...): ...

DOC: str
