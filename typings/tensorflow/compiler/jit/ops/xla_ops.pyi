from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def xla_cluster_output(input: Any, name: Optional[Any] = ...): ...

XlaClusterOutput: Any

def xla_cluster_output_eager_fallback(input: Any, name: Any, ctx: Any): ...
def xla_launch(constants: Any, args: Any, resources: Any, Tresults: Any, function: Any, name: Optional[Any] = ...): ...

XlaLaunch: Any

def xla_launch_eager_fallback(constants: Any, args: Any, resources: Any, Tresults: Any, function: Any, name: Any, ctx: Any): ...
