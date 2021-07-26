from collections import namedtuple
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import compat as compat
from typing import Any, Optional

VSpace = namedtuple('VSpace', ['aggregate_fn', 'num_elements_fn', 'zeros_fn', 'ones_fn', 'zeros_like_fn', 'ones_like_fn', 'graph_shape_fn'])

def imperative_grad(tape: Any, target: Any, sources: Any, output_gradients: Optional[Any] = ..., sources_raw: Optional[Any] = ..., unconnected_gradients: Any = ...): ...
