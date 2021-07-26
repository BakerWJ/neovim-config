from tensorflow.python.keras.layers import normalization as keras_normalization
from tensorflow.python.layers import base as base
from tensorflow.python.ops import init_ops as init_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class BatchNormalization(keras_normalization.BatchNormalization, base.Layer):
    def __init__(self, axis: int = ..., momentum: float = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer: Any = ..., gamma_initializer: Any = ..., moving_mean_initializer: Any = ..., moving_variance_initializer: Any = ..., beta_regularizer: Optional[Any] = ..., gamma_regularizer: Optional[Any] = ..., beta_constraint: Optional[Any] = ..., gamma_constraint: Optional[Any] = ..., renorm: bool = ..., renorm_clipping: Optional[Any] = ..., renorm_momentum: float = ..., fused: Optional[Any] = ..., trainable: bool = ..., virtual_batch_size: Optional[Any] = ..., adjustment: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: bool = ...): ...

def batch_normalization(inputs: Any, axis: int = ..., momentum: float = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer: Any = ..., gamma_initializer: Any = ..., moving_mean_initializer: Any = ..., moving_variance_initializer: Any = ..., beta_regularizer: Optional[Any] = ..., gamma_regularizer: Optional[Any] = ..., beta_constraint: Optional[Any] = ..., gamma_constraint: Optional[Any] = ..., training: bool = ..., trainable: bool = ..., name: Optional[Any] = ..., reuse: Optional[Any] = ..., renorm: bool = ..., renorm_clipping: Optional[Any] = ..., renorm_momentum: float = ..., fused: Optional[Any] = ..., virtual_batch_size: Optional[Any] = ..., adjustment: Optional[Any] = ...): ...
BatchNorm = BatchNormalization
batch_norm = batch_normalization
