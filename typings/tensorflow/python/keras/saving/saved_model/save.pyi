from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.keras.saving import saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import save_impl as save_impl
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from typing import Any, Optional

base_layer: Any
training_lib: Any

def save(model: Any, filepath: Any, overwrite: Any, include_optimizer: Any, signatures: Optional[Any] = ..., options: Optional[Any] = ...) -> None: ...
