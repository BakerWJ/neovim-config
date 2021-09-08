import abc
from tensorflow.python.distribute import parameter_server_strategy as parameter_server_strategy
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.keras import backend as backend, initializers as initializers
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.optimizer_v2 import learning_rate_schedule as learning_rate_schedule
from tensorflow.python.keras.utils import generic_utils as generic_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, control_flow_ops as control_flow_ops, gradients as gradients, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import revived_types as revived_types
from tensorflow.python.training.tracking import base as trackable, tracking as tracking
from tensorflow.python.util import nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class OptimizerV2(trackable.Trackable, metaclass=abc.ABCMeta):
    clipnorm: Any = ...
    clipvalue: Any = ...
    def __init__(self, name: Any, **kwargs: Any) -> None: ...
    def minimize(self, loss: Any, var_list: Any, grad_loss: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def get_gradients(self, loss: Any, params: Any): ...
    def apply_gradients(self, grads_and_vars: Any, name: Optional[Any] = ..., experimental_aggregate_gradients: bool = ...): ...
    def get_updates(self, loss: Any, params: Any): ...
    def __getattribute__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any) -> None: ...
    def get_slot_names(self): ...
    def add_slot(self, var: Any, slot_name: Any, initializer: str = ...): ...
    def get_slot(self, var: Any, slot_name: Any): ...
    @property
    def iterations(self): ...
    @iterations.setter
    def iterations(self, variable: Any) -> None: ...
    @abc.abstractmethod
    def get_config(self) -> Any: ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...
    def variables(self): ...
    @property
    def weights(self): ...
    def get_weights(self): ...
    def set_weights(self, weights: Any) -> None: ...
    def add_weight(self, name: Any, shape: Any, dtype: Optional[Any] = ..., initializer: str = ..., trainable: Optional[Any] = ..., synchronization: Any = ..., aggregation: Any = ...): ...

class RestoredOptimizer(OptimizerV2):
    def __init__(self) -> None: ...
    def get_config(self) -> None: ...