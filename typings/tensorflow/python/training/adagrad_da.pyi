from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class AdagradDAOptimizer(optimizer.Optimizer):
    def __init__(self, learning_rate: Any, global_step: Any, initial_gradient_squared_accumulator_value: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., use_locking: bool = ..., name: str = ...) -> None: ...
