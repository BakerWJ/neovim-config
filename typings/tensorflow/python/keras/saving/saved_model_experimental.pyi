from tensorflow.python.client import session as session
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import optimizers as optimizers
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.keras.saving import model_config as model_config, saving_utils as saving_utils
from tensorflow.python.keras.utils import mode_keys as mode_keys
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.saved_model import constants as constants, model_utils as model_utils
from tensorflow.python.training.tracking import graph_view as graph_view
from tensorflow.python.util import compat as compat, deprecation as deprecation, nest as nest
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

metrics_lib: Any
models_lib: Any
sequential: Any

def export_saved_model(model: Any, saved_model_path: Any, custom_objects: Optional[Any] = ..., as_text: bool = ..., input_signature: Optional[Any] = ..., serving_only: bool = ...) -> None: ...
def create_placeholder(spec: Any): ...
def load_from_saved_model(saved_model_path: Any, custom_objects: Optional[Any] = ...): ...
