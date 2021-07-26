from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import step_fn as step_fn
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.layers import core as core, normalization as normalization
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from typing import Any

def single_loss_example(optimizer_fn: Any, distribution: Any, use_bias: bool = ..., iterations_per_step: int = ...): ...
def minimize_loss_example(optimizer: Any, use_bias: bool = ..., use_callable_loss: bool = ...): ...
def batchnorm_example(optimizer_fn: Any, batch_per_epoch: int = ..., momentum: float = ..., renorm: bool = ..., update_ops_in_replica_mode: bool = ...): ...
