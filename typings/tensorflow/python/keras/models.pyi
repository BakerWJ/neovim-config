from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import optimizers as optimizers
from tensorflow.python.keras.engine import network as network, sequential as sequential, training as training, training_v1 as training_v1
from tensorflow.python.keras.engine.base_layer import AddMetric as AddMetric, Layer as Layer
from tensorflow.python.keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from tensorflow.python.keras.engine.network import Network as Network
from tensorflow.python.keras.saving import model_config as model_config, save as save
from tensorflow.python.keras.utils import generic_utils as generic_utils, version_utils as version_utils
from tensorflow.python.keras.utils.generic_utils import CustomObjectScope as CustomObjectScope
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

Model = training.Model
Sequential = sequential.Sequential
save_model = save.save_model
load_model = save.load_model
model_from_config = model_config.model_from_config
model_from_yaml = model_config.model_from_yaml
model_from_json = model_config.model_from_json

def share_weights(layer: Any): ...
def clone_model(model: Any, input_tensors: Optional[Any] = ..., clone_function: Optional[Any] = ...): ...
def in_place_subclassed_model_state_restoration(model: Any) -> None: ...
def clone_and_build_model(model: Any, input_tensors: Optional[Any] = ..., target_tensors: Optional[Any] = ..., custom_objects: Optional[Any] = ..., compile_clone: bool = ..., in_place_reset: bool = ..., optimizer_iterations: Optional[Any] = ..., optimizer_config: Optional[Any] = ...): ...
