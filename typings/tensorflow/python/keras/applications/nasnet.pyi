from tensorflow.python.keras import backend as backend, layers as layers
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

BASE_WEIGHTS_PATH: str
NASNET_MOBILE_WEIGHT_PATH: Any
NASNET_MOBILE_WEIGHT_PATH_NO_TOP: Any
NASNET_LARGE_WEIGHT_PATH: Any
NASNET_LARGE_WEIGHT_PATH_NO_TOP: Any

def NASNet(input_shape: Optional[Any] = ..., penultimate_filters: int = ..., num_blocks: int = ..., stem_block_filters: int = ..., skip_reduction: bool = ..., filter_multiplier: int = ..., include_top: bool = ..., weights: Optional[Any] = ..., input_tensor: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., default_size: Optional[Any] = ..., classifier_activation: str = ...): ...
def NASNetMobile(input_shape: Optional[Any] = ..., include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ...): ...
def NASNetLarge(input_shape: Optional[Any] = ..., include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ...): ...
def preprocess_input(x: Any, data_format: Optional[Any] = ...): ...
def decode_predictions(preds: Any, top: int = ...): ...
