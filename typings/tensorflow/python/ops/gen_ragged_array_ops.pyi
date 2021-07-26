from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_RaggedGatherOutput = namedtuple('RaggedGather', ['output_nested_splits', 'output_dense_values'])

def ragged_gather(params_nested_splits: Any, params_dense_values: Any, indices: Any, OUTPUT_RAGGED_RANK: Any, name: Optional[Any] = ...): ...

RaggedGather: Any

def ragged_gather_eager_fallback(params_nested_splits: Any, params_dense_values: Any, indices: Any, OUTPUT_RAGGED_RANK: Any, name: Any, ctx: Any): ...
