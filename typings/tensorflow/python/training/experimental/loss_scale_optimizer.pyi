from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops, smart_cond as smart_cond
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class MixedPrecisionLossScaleOptimizer(optimizer.Optimizer):
    def __init__(self, opt: Any, loss_scale: Any) -> None: ...
    def compute_gradients(self, loss: Any, var_list: Optional[Any] = ..., gate_gradients: Any = ..., aggregation_method: Optional[Any] = ..., colocate_gradients_with_ops: bool = ..., grad_loss: Optional[Any] = ...): ...
    def apply_gradients(self, grads_and_vars: Any, global_step: Optional[Any] = ..., name: Optional[Any] = ...): ...
