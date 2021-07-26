from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.training import training_ops as training_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class SGD(optimizer_v2.OptimizerV2):
    nesterov: Any = ...
    def __init__(self, learning_rate: float = ..., momentum: float = ..., nesterov: bool = ..., name: str = ..., **kwargs: Any) -> None: ...
    def get_config(self): ...
