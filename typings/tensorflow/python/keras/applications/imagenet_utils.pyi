from tensorflow.python.keras import activations as activations, backend as backend
from tensorflow.python.keras.utils import data_utils as data_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

CLASS_INDEX: Any
CLASS_INDEX_PATH: str
PREPROCESS_INPUT_DOC: str
PREPROCESS_INPUT_MODE_DOC: str
PREPROCESS_INPUT_RET_DOC_TF: str
PREPROCESS_INPUT_RET_DOC_TORCH: str
PREPROCESS_INPUT_RET_DOC_CAFFE: str

def preprocess_input(x: Any, data_format: Optional[Any] = ..., mode: str = ...): ...
def decode_predictions(preds: Any, top: int = ...): ...
def obtain_input_shape(input_shape: Any, default_size: Any, min_size: Any, data_format: Any, require_flatten: Any, weights: Optional[Any] = ...): ...
def correct_pad(inputs: Any, kernel_size: Any): ...
def validate_activation(classifier_activation: Any, weights: Any) -> None: ...
