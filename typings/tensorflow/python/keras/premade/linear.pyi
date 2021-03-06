from tensorflow.python.keras import activations as activations, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine import base_layer as base_layer, training as training
from tensorflow.python.keras.layers import core as core
from tensorflow.python.ops import nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class LinearModel(training.Model):
    units: Any = ...
    activation: Any = ...
    use_bias: Any = ...
    kernel_initializer: Any = ...
    bias_initializer: Any = ...
    kernel_regularizer: Any = ...
    bias_regularizer: Any = ...
    def __init__(self, units: int = ..., activation: Optional[Any] = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Optional[Any] = ..., bias_regularizer: Optional[Any] = ..., **kwargs: Any) -> None: ...
    dense_layers: Any = ...
    bias: Any = ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...
