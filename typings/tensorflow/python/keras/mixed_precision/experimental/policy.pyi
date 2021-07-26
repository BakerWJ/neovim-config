from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.mixed_precision.experimental import device_compatibility_check as device_compatibility_check
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training.experimental import mixed_precision_global_state as mixed_precision_global_state
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

USE_DEFAULT: str

class Policy:
    def __init__(self, name: Any, loss_scale: Any = ...) -> None: ...
    @property
    def variable_dtype(self): ...
    @property
    def compute_dtype(self): ...
    @property
    def should_cast_variables(self): ...
    @property
    def loss_scale(self): ...
    @property
    def name(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...

def global_policy(): ...
def policy_defaults_to_floatx(): ...
def set_policy(policy: Any) -> None: ...
def policy_scope(policy: Any) -> None: ...
def serialize(policy: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
