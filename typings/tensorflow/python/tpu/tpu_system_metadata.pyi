from collections import namedtuple
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.distribute import device_util as device_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, errors as errors, ops as ops
from tensorflow.python.tpu import tpu as tpu
from typing import Any

_TPUSystemMetadata = namedtuple('_TPUSystemMetadata', ['num_cores', 'num_hosts', 'num_of_cores_per_host', 'topology', 'devices'])

def get_session_config_with_timeout(timeout_in_secs: Any, cluster_def: Any): ...
def master_job(master: Any, cluster_def: Any): ...
