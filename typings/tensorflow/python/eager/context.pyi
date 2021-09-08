import threading
from collections import namedtuple
from tensorflow.core.framework import function_pb2 as function_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe, tf2 as tf2
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.eager import executor as executor, monitoring as monitoring
from tensorflow.python.framework import c_api_util as c_api_util
from tensorflow.python.util import compat as compat, is_in_graph_mode as is_in_graph_mode, tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

GRAPH_MODE: int
EAGER_MODE: int
default_execution_mode: Any
DEVICE_PLACEMENT_EXPLICIT: Any
DEVICE_PLACEMENT_WARN: Any
DEVICE_PLACEMENT_SILENT: Any
DEVICE_PLACEMENT_SILENT_FOR_INT32: Any
SYNC: int
ASYNC: int
MIRRORING_NONE: Any
MIRRORING_ALL: Any

class _EagerTensorCache:
    def __init__(self, max_items: int = ..., max_tensor_size: int = ...) -> None: ...
    def put(self, key: Any, value: Any) -> None: ...
    def get(self, key: Any): ...
    def flush(self) -> None: ...

class FunctionCallOptions:
    def __init__(self, executor_type: Optional[Any] = ..., config_proto: Optional[Any] = ...) -> None: ...
    @property
    def executor_type(self): ...
    @executor_type.setter
    def executor_type(self, executor_type: Any) -> None: ...
    @property
    def config_proto_serialized(self): ...
    @config_proto_serialized.setter
    def config_proto_serialized(self, config: Any) -> None: ...

class _TensorCaches(threading.local):
    def __init__(self) -> None: ...
    @property
    def ones_rank_cache(self): ...
    @property
    def zeros_cache(self): ...

class _ThreadLocalData(threading.local):
    device_spec: Any = ...
    device_name: str = ...
    is_eager: Any = ...
    scope_name: str = ...
    function_call_options: Any = ...
    executor: Any = ...
    op_callbacks: Any = ...
    invoking_op_callbacks: bool = ...
    def __init__(self) -> None: ...

ContextSwitch = namedtuple('ContextSwitch', ['is_building_function', 'enter_context_fn', 'device_stack'])

class _ContextSwitchStack(threading.local):
    stack: Any = ...
    def __init__(self, eager: Any) -> None: ...
    def push(self, is_building_function: Any, enter_context_fn: Any, device_stack: Any) -> None: ...
    def pop(self) -> None: ...

class LogicalDevice: ...

class LogicalDeviceConfiguration:
    def __new__(cls, memory_limit: Optional[Any] = ...): ...

class PhysicalDevice: ...

class _AtomicCounter:
    def __init__(self) -> None: ...
    def increment_and_get(self): ...

class _TensorCacheDeleter:
    def __init__(self, context_id: Any) -> None: ...
    def __del__(self) -> None: ...

class Context:
    def __init__(self, config: Optional[Any] = ..., device_policy: Optional[Any] = ..., execution_mode: Optional[Any] = ..., server_def: Optional[Any] = ...) -> None: ...
    def ensure_initialized(self) -> None: ...
    def get_server_def(self): ...
    def set_server_def(self, server_def: Any, keep_alive_secs: Any = ...) -> None: ...
    def update_server_def(self, server_def: Any, keep_alive_secs: Any = ...) -> None: ...
    def check_alive(self, worker_name: Any): ...
    def sync_executors(self) -> None: ...
    def clear_executor_errors(self) -> None: ...
    def enable_collective_ops(self, server_def: Any) -> None: ...
    def configure_collective_ops(self, collective_leader: str = ..., scoped_allocator_enabled_ops: Any = ..., use_nccl_communication: bool = ..., device_filters: Optional[Any] = ...) -> None: ...
    def executing_eagerly(self): ...
    def ones_rank_cache(self): ...
    def zeros_cache(self): ...
    @property
    def scope_name(self): ...
    @scope_name.setter
    def scope_name(self, s: Any) -> None: ...
    @property
    def device_name(self): ...
    @property
    def device_spec(self): ...
    def device(self, name: Any): ...
    def devices(self): ...
    def host_address_space(self): ...
    @property
    def execution_mode(self): ...
    @execution_mode.setter
    def execution_mode(self, mode: Any) -> None: ...
    def is_async(self): ...
    @property
    def executor(self): ...
    @executor.setter
    def executor(self, e: Any) -> None: ...
    @property
    def config(self): ...
    @property
    def function_call_options(self): ...
    @function_call_options.setter
    def function_call_options(self, options: Any) -> None: ...
    def num_gpus(self): ...
    def add_function(self, fn: Any) -> None: ...
    def add_function_def(self, fdef: Any) -> None: ...
    def get_function_def(self, name: Any): ...
    def remove_function(self, name: Any) -> None: ...
    def has_function(self, name: Any): ...
    def add_op_callback(self, callback: Any) -> None: ...
    def remove_op_callback(self, callback: Any) -> None: ...
    @property
    def op_callbacks(self): ...
    @property
    def invoking_op_callbacks(self): ...
    @invoking_op_callbacks.setter
    def invoking_op_callbacks(self, value: Any) -> None: ...
    def list_physical_devices(self, device_type: Optional[Any] = ...): ...
    def list_logical_devices(self, device_type: Optional[Any] = ...): ...
    def get_visible_devices(self, device_type: Optional[Any] = ...): ...
    def set_visible_devices(self, devices: Any, device_type: Optional[Any] = ...) -> None: ...
    def get_memory_growth(self, dev: Any): ...
    def set_memory_growth(self, dev: Any, enable: Any) -> None: ...
    def get_logical_device_configuration(self, dev: Any): ...
    def set_logical_device_configuration(self, dev: Any, virtual_devices: Any) -> None: ...
    @property
    def enable_mlir_bridge(self): ...
    @enable_mlir_bridge.setter
    def enable_mlir_bridge(self, enabled: Any) -> None: ...
    @property
    def optimizer_jit(self): ...
    @optimizer_jit.setter
    def optimizer_jit(self, enabled: Any) -> None: ...
    def get_optimizer_experimental_options(self): ...
    def set_optimizer_experimental_options(self, options: Any) -> None: ...
    @property
    def intra_op_parallelism_threads(self): ...
    @intra_op_parallelism_threads.setter
    def intra_op_parallelism_threads(self, num_threads: Any) -> None: ...
    @property
    def inter_op_parallelism_threads(self): ...
    @inter_op_parallelism_threads.setter
    def inter_op_parallelism_threads(self, num_threads: Any) -> None: ...
    @property
    def soft_device_placement(self): ...
    @soft_device_placement.setter
    def soft_device_placement(self, enabled: Any) -> None: ...
    @property
    def log_device_placement(self): ...
    @log_device_placement.setter
    def log_device_placement(self, enabled: Any) -> None: ...
    @property
    def device_policy(self): ...
    @device_policy.setter
    def device_policy(self, policy: Any) -> None: ...
    @property
    def mirroring_policy(self): ...
    @mirroring_policy.setter
    def mirroring_policy(self, policy: Any) -> None: ...
    @property
    def lazy_remote_inputs_copy(self): ...
    @lazy_remote_inputs_copy.setter
    def lazy_remote_inputs_copy(self, lazy_copy: Any) -> None: ...
    def enable_run_metadata(self) -> None: ...
    def disable_run_metadata(self) -> None: ...
    def enable_graph_collection(self) -> None: ...
    def disable_graph_collection(self) -> None: ...
    def export_run_metadata(self): ...
    @property
    def context_switches(self): ...
    def start_step(self) -> None: ...
    def end_step(self) -> None: ...

class _EagerDeviceContext:
    def __init__(self, ctx: Any, device_name: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *ex_info: Any) -> None: ...

def context(): ...
def context_safe(): ...
def ensure_initialized() -> None: ...
def set_global_seed(seed: Any) -> None: ...
def global_seed(): ...
def internal_operation_seed(): ...
def executing_eagerly(): ...
def executing_eagerly_v1(): ...
def in_eager_mode(): ...
def shared_name(name: Optional[Any] = ...): ...
def graph_mode(): ...
def eager_mode(): ...
def scope_name(): ...
def device(name: Any): ...
def get_log_device_placement(): ...
def set_log_device_placement(enabled: Any) -> None: ...
def device_policy(policy: Any) -> None: ...
def mirroring_policy(policy: Any) -> None: ...
def set_execution_mode(mode: Any) -> None: ...
def execution_mode(mode: Any) -> None: ...
def executor_scope(e: Any) -> None: ...
def function_executor_type(executor_type: Any) -> None: ...
def is_async(): ...
def num_gpus(): ...
def enable_run_metadata() -> None: ...
def disable_run_metadata() -> None: ...
def enable_graph_collection() -> None: ...
def disable_graph_collection() -> None: ...
def export_run_metadata(): ...
def collect_graphs(optimized: bool = ...) -> None: ...
def get_server_def(): ...
def set_server_def(server_def: Any) -> None: ...
def update_server_def(server_def: Any) -> None: ...
def check_alive(worker_name: Any): ...
def async_scope() -> None: ...
def async_wait() -> None: ...
def async_clear_error() -> None: ...
def add_function(fdef: Any) -> None: ...
def remove_function(name: Any) -> None: ...
def get_function_def(name: Any): ...