from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import optimizer as optimizer, queue_runner as queue_runner, session_manager as session_manager, session_run_hook as session_run_hook
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class SyncReplicasOptimizer(optimizer.Optimizer):
    def __init__(self, opt: Any, replicas_to_aggregate: Any, total_num_replicas: Optional[Any] = ..., variable_averages: Optional[Any] = ..., variables_to_average: Optional[Any] = ..., use_locking: bool = ..., name: str = ...) -> None: ...
    def compute_gradients(self, *args: Any, **kwargs: Any): ...
    local_step_init_op: Any = ...
    ready_for_local_init_op: Any = ...
    chief_init_op: Any = ...
    def apply_gradients(self, grads_and_vars: Any, global_step: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def get_chief_queue_runner(self): ...
    def get_slot(self, *args: Any, **kwargs: Any): ...
    def variables(self): ...
    def get_slot_names(self, *args: Any, **kwargs: Any): ...
    def get_init_tokens_op(self, num_tokens: int = ...): ...
    def make_session_run_hook(self, is_chief: Any, num_tokens: int = ...): ...

class _SyncReplicasOptimizerHook(session_run_hook.SessionRunHook):
    def __init__(self, sync_optimizer: Any, is_chief: Any, num_tokens: Any) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
