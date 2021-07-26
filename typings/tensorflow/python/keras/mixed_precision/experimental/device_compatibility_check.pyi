from tensorflow.python.client import device_lib as device_lib
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, gpu_util as gpu_util
from tensorflow.python.platform import tf_logging as tf_logging
from typing import Any

def log_device_compatibility_check(policy_name: Any, skip_local: Any) -> None: ...
