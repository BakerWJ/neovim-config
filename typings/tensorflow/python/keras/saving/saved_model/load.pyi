from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, tensor_spec as tensor_spec
from tensorflow.python.keras import backend as backend, regularizers as regularizers
from tensorflow.python.keras.engine import input_spec as input_spec
from tensorflow.python.keras.saving import saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import constants as constants, json_utils as json_utils, utils as utils
from tensorflow.python.keras.saving.saved_model.serialized_attributes import CommonEndpoints as CommonEndpoints
from tensorflow.python.keras.utils import generic_utils as generic_utils, metrics_utils as metrics_utils
from tensorflow.python.saved_model import load as tf_load, nested_structure_coder as nested_structure_coder, revived_types as revived_types
from tensorflow.python.training.tracking.tracking import delete_tracking as delete_tracking
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from typing import Any, Optional

models_lib: Any
base_layer: Any
layers_module: Any
input_layer: Any
network_lib: Any
training_lib: Any
training_lib_v1: Any
metrics: Any
recurrent: Any
PUBLIC_ATTRIBUTES: Any
KERAS_OBJECT_IDENTIFIERS: Any

def load(path: Any, compile: bool = ...): ...

class KerasObjectLoader(tf_load.Loader):
    model_layer_dependencies: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def revive_custom_object(identifier: Any, metadata: Any): ...

class RevivedLayer:
    @property
    def keras_api(self): ...
    def get_config(self): ...

class RevivedInputLayer:
    def get_config(self): ...

def recursively_deserialize_keras_object(config: Any, module_objects: Optional[Any] = ...): ...
def infer_inputs_from_restored_call_function(fn: Any): ...

class RevivedNetwork(RevivedLayer): ...
