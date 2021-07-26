import enum
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import collective_util as collective_util, device_util as device_util, distribution_strategy_context as distribution_strategy_context, numpy_dataset as numpy_dataset, reduce_util as reduce_util
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, custom_gradient as custom_gradient, math_ops as math_ops, resource_variable_ops as resource_variable_ops, summary_ops_v2 as summary_ops_v2, variable_scope as variable_scope
from tensorflow.python.ops.losses import loss_reduction as loss_reduction, losses_impl as losses_impl
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import deprecation as deprecation, nest as nest, tf_contextlib as tf_contextlib
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any, Optional

def get_update_replica_id(): ...

class UpdateContext:
    def __init__(self, replica_id: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...

def get_loss_reduction(): ...
def require_replica_context(replica_ctx: Any) -> None: ...

class _CurrentDistributionContext:
    def __init__(self, strategy: Any, var_creator_scope: Any, var_scope: Optional[Any] = ..., default_device: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...

class InputReplicationMode(enum.Enum):
    PER_WORKER: str = ...

class InputContext:
    def __init__(self, num_input_pipelines: int = ..., input_pipeline_id: int = ..., num_replicas_in_sync: int = ...) -> None: ...
    @property
    def num_replicas_in_sync(self): ...
    @property
    def input_pipeline_id(self): ...
    @property
    def num_input_pipelines(self): ...
    def get_per_replica_batch_size(self, global_batch_size: Any): ...

class ValueContext:
    def __init__(self, replica_id_in_sync_group: int = ..., num_replicas_in_sync: int = ...) -> None: ...
    @property
    def num_replicas_in_sync(self): ...
    @property
    def replica_id_in_sync_group(self): ...

class RunOptions:
    def __new__(cls, experimental_enable_dynamic_batch_size: bool = ..., experimental_bucketizing_dynamic_shape: bool = ...): ...

class StrategyBase:
    def __init__(self, extended: Any) -> None: ...
    @property
    def extended(self): ...
    def scope(self): ...
    def colocate_vars_with(self, colocate_with_variable: Any): ...
    def make_dataset_iterator(self, dataset: Any): ...
    def make_input_fn_iterator(self, input_fn: Any, replication_mode: Any = ...): ...
    def experimental_make_numpy_dataset(self, numpy_input: Any): ...
    def experimental_run(self, fn: Any, input_iterator: Optional[Any] = ...): ...
    def experimental_distribute_dataset(self, dataset: Any): ...
    def experimental_distribute_datasets_from_function(self, dataset_fn: Any): ...
    def run(self, fn: Any, args: Any = ..., kwargs: Optional[Any] = ..., options: Optional[Any] = ...): ...
    def experimental_run_v2(self, fn: Any, args: Any = ..., kwargs: Optional[Any] = ..., options: Optional[Any] = ...): ...
    def reduce(self, reduce_op: Any, value: Any, axis: Any): ...
    def unwrap(self, value: Any): ...
    def experimental_local_results(self, value: Any): ...
    def group(self, value: Any, name: Optional[Any] = ...): ...
    @property
    def num_replicas_in_sync(self): ...
    def configure(self, session_config: Optional[Any] = ..., cluster_spec: Optional[Any] = ..., task_type: Optional[Any] = ..., task_id: Optional[Any] = ...): ...
    def update_config_proto(self, config_proto: Any): ...
    def __deepcopy__(self, memo: Any): ...
    def __copy__(self) -> None: ...

class Strategy(StrategyBase):
    __doc__: Any = ...
    def experimental_assign_to_logical_device(self, tensor: Any, logical_device_id: Any): ...
    def experimental_split_to_logical_devices(self, tensor: Any, partition_dimensions: Any): ...
    def experimental_replicate_to_logical_devices(self, tensor: Any): ...
    def experimental_distribute_values_from_function(self, value_fn: Any): ...

class StrategyV1(StrategyBase):
    def make_dataset_iterator(self, dataset: Any): ...
    def make_input_fn_iterator(self, input_fn: Any, replication_mode: Any = ...): ...
    def experimental_make_numpy_dataset(self, numpy_input: Any, session: Optional[Any] = ...): ...
    def experimental_run(self, fn: Any, input_iterator: Optional[Any] = ...): ...
    def reduce(self, reduce_op: Any, value: Any, axis: Optional[Any] = ...): ...
    def update_config_proto(self, config_proto: Any): ...

class StrategyExtendedV2:
    def __init__(self, container_strategy: Any) -> None: ...
    def variable_created_in_scope(self, v: Any): ...
    def colocate_vars_with(self, colocate_with_variable: Any): ...
    def reduce_to(self, reduce_op: Any, value: Any, destinations: Any, experimental_hints: Optional[Any] = ...): ...
    def batch_reduce_to(self, reduce_op: Any, value_destination_pairs: Any, experimental_hints: Optional[Any] = ...): ...
    def update(self, var: Any, fn: Any, args: Any = ..., kwargs: Optional[Any] = ..., group: bool = ...): ...
    def update_non_slot(self, colocate_with: Any, fn: Any, args: Any = ..., kwargs: Optional[Any] = ..., group: bool = ...): ...
    def value_container(self, value: Any) -> None: ...
    @property
    def experimental_require_static_shapes(self): ...
    @property
    def worker_devices(self) -> None: ...
    @property
    def parameter_devices(self) -> None: ...
    def non_slot_devices(self, var_list: Any) -> None: ...

class StrategyExtendedV1(StrategyExtendedV2):
    __doc__: Any = ...
    def experimental_make_numpy_dataset(self, numpy_input: Any, session: Optional[Any] = ...): ...
    def broadcast_to(self, tensor: Any, destinations: Any): ...
    def experimental_run_steps_on_iterator(self, fn: Any, iterator: Any, iterations: int = ..., initial_loop_values: Optional[Any] = ...): ...
    def call_for_each_replica(self, fn: Any, args: Any = ..., kwargs: Optional[Any] = ...): ...
    def read_var(self, v: Any) -> None: ...
    @property
    def experimental_between_graph(self) -> None: ...
    @property
    def experimental_should_init(self) -> None: ...
    @property
    def should_checkpoint(self) -> None: ...
    @property
    def should_save_summary(self) -> None: ...

class ReplicaContext:
    def __init__(self, strategy: Any, replica_id_in_sync_group: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...
    def merge_call(self, merge_fn: Any, args: Any = ..., kwargs: Optional[Any] = ...): ...
    @property
    def num_replicas_in_sync(self): ...
    @property
    def replica_id_in_sync_group(self): ...
    @property
    def strategy(self): ...
    @property
    def devices(self): ...
    def all_reduce(self, reduce_op: Any, value: Any, experimental_hints: Optional[Any] = ...): ...

class _DefaultDistributionStrategy(StrategyV1):
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo: Any) -> None: ...

class _DefaultDistributionContext:
    def __init__(self, strategy: Any): ...
    def __enter__(self): ...
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...

class _DefaultDistributionExtended(StrategyExtendedV1):
    def __init__(self, container_strategy: Any) -> None: ...
    def colocate_vars_with(self, colocate_with_variable: Any): ...
    def variable_created_in_scope(self, v: Any): ...
    def read_var(self, replica_local_var: Any): ...
    def value_container(self, value: Any): ...
    @property
    def worker_devices(self) -> None: ...
    @property
    def parameter_devices(self) -> None: ...
    def non_slot_devices(self, var_list: Any): ...
    class DefaultInputIterator:
        def __init__(self, dataset: Any) -> None: ...
        def get_next(self): ...
        def initialize(self): ...
        @property
        def initializer(self): ...

distribution_strategy_gauge: Any
distribution_strategy_replica_gauge: Any
