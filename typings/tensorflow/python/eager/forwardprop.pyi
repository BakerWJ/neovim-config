from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import backprop as backprop, backprop_util as backprop_util, def_function as def_function, execute as execute, forwardprop_util as forwardprop_util
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class ForwardAccumulator:
    def __init__(self, primals: Any, tangents: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, typ: Any, value: Any, traceback: Any) -> None: ...
    def jvp(self, primals: Any, unconnected_gradients: Any = ...): ...
