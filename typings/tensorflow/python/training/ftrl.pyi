from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class FtrlOptimizer(optimizer.Optimizer):
    def __init__(self, learning_rate: Any, learning_rate_power: Any = ..., initial_accumulator_value: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., use_locking: bool = ..., name: str = ..., accum_name: Optional[Any] = ..., linear_name: Optional[Any] = ..., l2_shrinkage_regularization_strength: float = ...) -> None: ...
