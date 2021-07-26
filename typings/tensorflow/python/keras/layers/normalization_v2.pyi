from tensorflow.python.distribute import reduce_util as reduce_util
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras.layers import normalization as normalization
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class SyncBatchNormalization(normalization.BatchNormalizationBase):
    def __init__(self, axis: int = ..., momentum: float = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer: str = ..., gamma_initializer: str = ..., moving_mean_initializer: str = ..., moving_variance_initializer: str = ..., beta_regularizer: Optional[Any] = ..., gamma_regularizer: Optional[Any] = ..., beta_constraint: Optional[Any] = ..., gamma_constraint: Optional[Any] = ..., renorm: bool = ..., renorm_clipping: Optional[Any] = ..., renorm_momentum: float = ..., trainable: bool = ..., adjustment: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...

class BatchNormalization(normalization.BatchNormalizationBase):
    __doc__: Any = ...
