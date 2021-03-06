from collections import namedtuple
from tensorflow.python.distribute.cluster_resolver import cluster_resolver as cluster_resolver
from tensorflow.python.framework import errors as errors
from tensorflow.python.tpu.client import client as client
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def is_running_in_gce(): ...

DeviceDetails = namedtuple('DeviceDetails', ['device_map', 'total_cores'])

class TPUClusterResolver(cluster_resolver.ClusterResolver):
    task_type: Any = ...
    task_id: int = ...
    def __init__(self, tpu: Optional[Any] = ..., zone: Optional[Any] = ..., project: Optional[Any] = ..., job_name: str = ..., coordinator_name: Optional[Any] = ..., coordinator_address: Optional[Any] = ..., credentials: str = ..., service: Optional[Any] = ..., discovery_url: Optional[Any] = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def master(self, task_type: Optional[Any] = ..., task_id: Optional[Any] = ..., rpc_layer: Optional[Any] = ...): ...
    def get_master(self): ...
    def get_job_name(self): ...
    def cluster_spec(self): ...
    def num_accelerators(self, task_type: Optional[Any] = ..., task_id: Optional[Any] = ..., config_proto: Optional[Any] = ...): ...
    @property
    def environment(self): ...
    def __deepcopy__(self, memo: Any): ...
