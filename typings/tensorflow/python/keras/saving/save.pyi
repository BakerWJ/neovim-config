from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.saving import hdf5_format as hdf5_format
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.saved_model import loader_impl as loader_impl
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

def save_model(model: Any, filepath: Any, overwrite: bool = ..., include_optimizer: bool = ..., save_format: Optional[Any] = ..., signatures: Optional[Any] = ..., options: Optional[Any] = ...) -> None: ...
def load_model(filepath: Any, custom_objects: Optional[Any] = ..., compile: bool = ...): ...
