from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras.optimizer_v2 import learning_rate_schedule as learning_rate_schedule
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def exponential_decay(learning_rate: Any, global_step: Any, decay_steps: Any, decay_rate: Any, staircase: bool = ..., name: Optional[Any] = ...): ...
def piecewise_constant(x: Any, boundaries: Any, values: Any, name: Optional[Any] = ...): ...
def polynomial_decay(learning_rate: Any, global_step: Any, decay_steps: Any, end_learning_rate: float = ..., power: float = ..., cycle: bool = ..., name: Optional[Any] = ...): ...
def natural_exp_decay(learning_rate: Any, global_step: Any, decay_steps: Any, decay_rate: Any, staircase: bool = ..., name: Optional[Any] = ...): ...
def inverse_time_decay(learning_rate: Any, global_step: Any, decay_steps: Any, decay_rate: Any, staircase: bool = ..., name: Optional[Any] = ...): ...
def cosine_decay(learning_rate: Any, global_step: Any, decay_steps: Any, alpha: float = ..., name: Optional[Any] = ...): ...
def cosine_decay_restarts(learning_rate: Any, global_step: Any, first_decay_steps: Any, t_mul: float = ..., m_mul: float = ..., alpha: float = ..., name: Optional[Any] = ...): ...
def linear_cosine_decay(learning_rate: Any, global_step: Any, decay_steps: Any, num_periods: float = ..., alpha: float = ..., beta: float = ..., name: Optional[Any] = ...): ...
def noisy_linear_cosine_decay(learning_rate: Any, global_step: Any, decay_steps: Any, initial_variance: float = ..., variance_decay: float = ..., num_periods: float = ..., alpha: float = ..., beta: float = ..., name: Optional[Any] = ...): ...
