from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras import backend_config as backend_config
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops
from tensorflow.python.training import training_ops as training_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class Adagrad(optimizer_v2.OptimizerV2):
    epsilon: Any = ...
    def __init__(self, learning_rate: float = ..., initial_accumulator_value: float = ..., epsilon: float = ..., name: str = ..., **kwargs: Any) -> None: ...
    def set_weights(self, weights: Any) -> None: ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...
    def get_config(self): ...
