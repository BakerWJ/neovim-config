from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.optimizer_v2 import ftrl as ftrl, optimizer_v2 as optimizer_v2
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.ops import clip_ops as clip_ops, math_ops as math_ops, state_ops as state_ops
from tensorflow.python.training import training_util as training_util
from tensorflow.python.training.tracking import base as trackable
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class Optimizer:
    updates: Any = ...
    weights: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def get_updates(self, loss: Any, params: Any) -> None: ...
    def get_gradients(self, loss: Any, params: Any): ...
    def set_weights(self, weights: Any) -> None: ...
    def get_weights(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any): ...

class SGD(Optimizer):
    iterations: Any = ...
    lr: Any = ...
    momentum: Any = ...
    decay: Any = ...
    initial_decay: Any = ...
    nesterov: Any = ...
    def __init__(self, lr: float = ..., momentum: float = ..., decay: float = ..., nesterov: bool = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class RMSprop(Optimizer):
    lr: Any = ...
    rho: Any = ...
    decay: Any = ...
    iterations: Any = ...
    epsilon: Any = ...
    initial_decay: Any = ...
    def __init__(self, lr: float = ..., rho: float = ..., epsilon: Optional[Any] = ..., decay: float = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class Adagrad(Optimizer):
    lr: Any = ...
    decay: Any = ...
    iterations: Any = ...
    epsilon: Any = ...
    initial_decay: Any = ...
    def __init__(self, lr: float = ..., epsilon: Optional[Any] = ..., decay: float = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class Adadelta(Optimizer):
    lr: Any = ...
    decay: Any = ...
    iterations: Any = ...
    rho: Any = ...
    epsilon: Any = ...
    initial_decay: Any = ...
    def __init__(self, lr: float = ..., rho: float = ..., epsilon: Optional[Any] = ..., decay: float = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class Adam(Optimizer):
    iterations: Any = ...
    lr: Any = ...
    beta_1: Any = ...
    beta_2: Any = ...
    decay: Any = ...
    epsilon: Any = ...
    initial_decay: Any = ...
    amsgrad: Any = ...
    def __init__(self, lr: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: Optional[Any] = ..., decay: float = ..., amsgrad: bool = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class Adamax(Optimizer):
    iterations: Any = ...
    lr: Any = ...
    beta_1: Any = ...
    beta_2: Any = ...
    decay: Any = ...
    epsilon: Any = ...
    initial_decay: Any = ...
    def __init__(self, lr: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: Optional[Any] = ..., decay: float = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class Nadam(Optimizer):
    iterations: Any = ...
    m_schedule: Any = ...
    lr: Any = ...
    beta_1: Any = ...
    beta_2: Any = ...
    epsilon: Any = ...
    schedule_decay: Any = ...
    def __init__(self, lr: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: Optional[Any] = ..., schedule_decay: float = ..., **kwargs: Any) -> None: ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    def get_config(self): ...

class TFOptimizer(Optimizer, trackable.Trackable):
    optimizer: Any = ...
    iterations: Any = ...
    def __init__(self, optimizer: Any, iterations: Optional[Any] = ...) -> None: ...
    def apply_gradients(self, grads: Any) -> None: ...
    def get_grads(self, loss: Any, params: Any): ...
    updates: Any = ...
    def get_updates(self, loss: Any, params: Any): ...
    @property
    def weights(self) -> None: ...
    def get_config(self) -> None: ...
    def from_config(self, config: Any) -> None: ...
sgd = SGD
rmsprop = RMSprop
adagrad = Adagrad
adadelta = Adadelta
adam = Adam
adamax = Adamax
nadam = Nadam

def serialize(optimizer: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
def get(identifier: Any): ...
