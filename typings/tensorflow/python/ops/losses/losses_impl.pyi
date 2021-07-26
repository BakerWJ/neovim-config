from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, confusion_matrix as confusion_matrix, control_flow_ops as control_flow_ops, math_ops as math_ops, nn as nn, nn_ops as nn_ops, weights_broadcast_ops as weights_broadcast_ops
from tensorflow.python.ops.losses import util as util
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args, deprecated_argument_lookup as deprecated_argument_lookup
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class Reduction:
    NONE: str = ...
    SUM: str = ...
    SUM_OVER_BATCH_SIZE: str = ...
    MEAN: str = ...
    SUM_BY_NONZERO_WEIGHTS: str = ...
    SUM_OVER_NONZERO_WEIGHTS: Any = ...
    @classmethod
    def all(cls): ...
    @classmethod
    def validate(cls, key: Any) -> None: ...

def compute_weighted_loss(losses: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def absolute_difference(labels: Any, predictions: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def cosine_distance(labels: Any, predictions: Any, axis: Optional[Any] = ..., weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ..., dim: Optional[Any] = ...): ...
def hinge_loss(labels: Any, logits: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def huber_loss(labels: Any, predictions: Any, weights: float = ..., delta: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def log_loss(labels: Any, predictions: Any, weights: float = ..., epsilon: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def mean_pairwise_squared_error(labels: Any, predictions: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ...): ...
def mean_squared_error(labels: Any, predictions: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def sigmoid_cross_entropy(multi_class_labels: Any, logits: Any, weights: float = ..., label_smoothing: int = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def softmax_cross_entropy(onehot_labels: Any, logits: Any, weights: float = ..., label_smoothing: int = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
def sparse_softmax_cross_entropy(labels: Any, logits: Any, weights: float = ..., scope: Optional[Any] = ..., loss_collection: Any = ..., reduction: Any = ...): ...
