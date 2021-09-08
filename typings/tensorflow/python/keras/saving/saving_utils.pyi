from tensorflow.python.eager import def_function as def_function
from tensorflow.python.keras import losses as losses, optimizers as optimizers
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from tensorflow.python.util import nest as nest
from typing import Any, Optional

def extract_model_metrics(model: Any): ...
def model_input_signature(model: Any, keep_original_batch_size: bool = ...): ...
def raise_model_input_error(model: Any) -> None: ...
def trace_model_call(model: Any, input_signature: Optional[Any] = ...): ...
def model_metadata(model: Any, include_optimizer: bool = ..., require_config: bool = ...): ...
def should_overwrite(filepath: Any, overwrite: Any): ...
def compile_args_from_training_config(training_config: Any, custom_objects: Optional[Any] = ...): ...