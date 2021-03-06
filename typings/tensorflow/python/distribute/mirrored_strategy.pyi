import threading
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, input_lib as input_lib, multi_worker_util as multi_worker_util, numpy_dataset as numpy_dataset, reduce_util as reduce_util, shared_variable_creator as shared_variable_creator, values as values
from tensorflow.python.distribute.cluster_resolver import TFConfigClusterResolver as TFConfigClusterResolver
from tensorflow.python.eager import context as context, def_function as def_function, tape as tape
from tensorflow.python.framework import config as config, constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, summary_ops_v2 as summary_ops_v2, variable_scope as variable_scope
from tensorflow.python.training import coordinator as coordinator
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _RequestedStop(Exception): ...

def all_local_devices(num_gpus: Optional[Any] = ...): ...
def all_devices(): ...

class MirroredStrategy(distribute_lib.Strategy):
    def __init__(self, devices: Optional[Any] = ..., cross_device_ops: Optional[Any] = ...) -> None: ...

class MirroredStrategyV1(distribute_lib.StrategyV1):
    __doc__: Any = ...
    def __init__(self, devices: Optional[Any] = ..., cross_device_ops: Optional[Any] = ...) -> None: ...

class MirroredExtended(distribute_lib.StrategyExtendedV1):
    experimental_enable_get_next_as_optional: bool = ...
    def __init__(self, container_strategy: Any, devices: Optional[Any] = ..., cross_device_ops: Optional[Any] = ...) -> None: ...
    def read_var(self, replica_local_var: Any): ...
    def value_container(self, val: Any): ...
    @property
    def worker_devices(self): ...
    @property
    def worker_devices_by_replica(self): ...
    @property
    def parameter_devices(self): ...
    @property
    def experimental_between_graph(self): ...
    @property
    def experimental_should_init(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
    def non_slot_devices(self, var_list: Any): ...

class _MirroredReplicaThread(threading.Thread):
    coord: Any = ...
    distribution: Any = ...
    devices: Any = ...
    replica_id: Any = ...
    variable_creator_fn: Any = ...
    main_fn: Any = ...
    main_args: Any = ...
    main_kwargs: Any = ...
    main_result: Any = ...
    done: bool = ...
    merge_fn: Any = ...
    merge_args: Any = ...
    merge_kwargs: Any = ...
    merge_result: Any = ...
    captured_name_scope: Any = ...
    captured_var_scope: Any = ...
    should_run: Any = ...
    has_paused: Any = ...
    in_eager: Any = ...
    context_device_policy: Any = ...
    graph: Any = ...
    def __init__(self, dist: Any, coord: Any, replica_id: Any, devices: Any, variable_creator_fn: Any, fn: Any, args: Any, kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def record_thread_local_summary_state(self) -> None: ...
    def restore_thread_local_summary_state(self) -> None: ...
    def record_thread_local_eager_context_state(self) -> None: ...
    def restore_thread_local_eager_context_state(self) -> None: ...

class MirroredReplicaContext(distribute_lib.ReplicaContext):
    @property
    def devices(self): ...
