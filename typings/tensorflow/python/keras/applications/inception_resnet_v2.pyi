from tensorflow.python.keras import backend as backend, layers as layers
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

BASE_WEIGHT_URL: str

def InceptionResNetV2(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., classifier_activation: str = ..., **kwargs: Any): ...
def conv2d_bn(x: Any, filters: Any, kernel_size: Any, strides: int = ..., padding: str = ..., activation: str = ..., use_bias: bool = ..., name: Optional[Any] = ...): ...
def inception_resnet_block(x: Any, scale: Any, block_type: Any, block_idx: Any, activation: str = ...): ...
def preprocess_input(x: Any, data_format: Optional[Any] = ...): ...
def decode_predictions(preds: Any, top: int = ...): ...
