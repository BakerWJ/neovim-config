from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, confusion_matrix as confusion_matrix, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.util import tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def squeeze_or_expand_dimensions(y_pred: Any, y_true: Optional[Any] = ..., sample_weight: Optional[Any] = ...): ...
def scale_losses_by_sample_weight(losses: Any, sample_weight: Any): ...
def check_per_example_loss_rank(per_example_loss: Any) -> None: ...
def add_loss(loss: Any, loss_collection: Any = ...) -> None: ...
def get_losses(scope: Optional[Any] = ..., loss_collection: Any = ...): ...
def get_regularization_losses(scope: Optional[Any] = ...): ...
def get_regularization_loss(scope: Optional[Any] = ..., name: str = ...): ...
def get_total_loss(add_regularization_losses: bool = ..., name: str = ..., scope: Optional[Any] = ...): ...