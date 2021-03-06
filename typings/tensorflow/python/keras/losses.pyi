import abc
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops, smart_cond as smart_cond, tensor_util as tensor_util
from tensorflow.python.keras.utils import losses_utils as losses_utils, tf_utils as tf_utils
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn
from tensorflow.python.ops.losses import losses_impl as losses_impl
from tensorflow.python.util.tf_export import keras_export as keras_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any, Optional

class Loss(metaclass=abc.ABCMeta):
    reduction: Any = ...
    name: Any = ...
    def __init__(self, reduction: Any = ..., name: Optional[Any] = ...) -> None: ...
    def __call__(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    @classmethod
    def from_config(cls, config: Any): ...
    def get_config(self): ...
    @abc.abstractmethod
    def call(self, y_true: Any, y_pred: Any) -> Any: ...

class LossFunctionWrapper(Loss):
    fn: Any = ...
    def __init__(self, fn: Any, reduction: Any = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, y_true: Any, y_pred: Any): ...
    def get_config(self): ...

class MeanSquaredError(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class MeanAbsoluteError(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class MeanAbsolutePercentageError(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class MeanSquaredLogarithmicError(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class BinaryCrossentropy(LossFunctionWrapper):
    from_logits: Any = ...
    def __init__(self, from_logits: bool = ..., label_smoothing: int = ..., reduction: Any = ..., name: str = ...) -> None: ...

class CategoricalCrossentropy(LossFunctionWrapper):
    def __init__(self, from_logits: bool = ..., label_smoothing: int = ..., reduction: Any = ..., name: str = ...) -> None: ...

class SparseCategoricalCrossentropy(LossFunctionWrapper):
    def __init__(self, from_logits: bool = ..., reduction: Any = ..., name: str = ...) -> None: ...

class Hinge(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class SquaredHinge(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class CategoricalHinge(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class Poisson(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class LogCosh(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class KLDivergence(LossFunctionWrapper):
    def __init__(self, reduction: Any = ..., name: str = ...) -> None: ...

class Huber(LossFunctionWrapper):
    def __init__(self, delta: float = ..., reduction: Any = ..., name: str = ...) -> None: ...

def mean_squared_error(y_true: Any, y_pred: Any): ...
def mean_absolute_error(y_true: Any, y_pred: Any): ...
def mean_absolute_percentage_error(y_true: Any, y_pred: Any): ...
def mean_squared_logarithmic_error(y_true: Any, y_pred: Any): ...
def squared_hinge(y_true: Any, y_pred: Any): ...
def hinge(y_true: Any, y_pred: Any): ...
def categorical_hinge(y_true: Any, y_pred: Any): ...
def huber_loss(y_true: Any, y_pred: Any, delta: float = ...): ...
def logcosh(y_true: Any, y_pred: Any): ...
def categorical_crossentropy(y_true: Any, y_pred: Any, from_logits: bool = ..., label_smoothing: int = ...): ...
def sparse_categorical_crossentropy(y_true: Any, y_pred: Any, from_logits: bool = ..., axis: int = ...): ...
def binary_crossentropy(y_true: Any, y_pred: Any, from_logits: bool = ..., label_smoothing: int = ...): ...
def kullback_leibler_divergence(y_true: Any, y_pred: Any): ...
def poisson(y_true: Any, y_pred: Any): ...
def cosine_similarity(y_true: Any, y_pred: Any, axis: int = ...): ...

class CosineSimilarity(LossFunctionWrapper):
    def __init__(self, axis: int = ..., reduction: Any = ..., name: str = ...) -> None: ...
bce = binary_crossentropy
BCE = binary_crossentropy
mse = mean_squared_error
MSE = mean_squared_error
mae = mean_absolute_error
MAE = mean_absolute_error
mape = mean_absolute_percentage_error
MAPE = mean_absolute_percentage_error
msle = mean_squared_logarithmic_error
MSLE = mean_squared_logarithmic_error
kld = kullback_leibler_divergence
KLD = kullback_leibler_divergence

def is_categorical_crossentropy(loss: Any): ...
def serialize(loss: Any): ...
def deserialize(name: Any, custom_objects: Optional[Any] = ...): ...
def get(identifier: Any): ...

LABEL_DTYPES_FOR_LOSSES: Any
