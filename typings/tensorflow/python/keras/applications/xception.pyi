from tensorflow.python.keras import backend as backend, layers as layers
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

TF_WEIGHTS_PATH: str
TF_WEIGHTS_PATH_NO_TOP: str

def Xception(include_top: bool = ..., weights: str = ..., input_tensor: Optional[Any] = ..., input_shape: Optional[Any] = ..., pooling: Optional[Any] = ..., classes: int = ..., classifier_activation: str = ...): ...
def preprocess_input(x: Any, data_format: Optional[Any] = ...): ...
def decode_predictions(preds: Any, top: int = ...): ...
