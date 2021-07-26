from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_RaggedRangeOutput = namedtuple('RaggedRange', ['rt_nested_splits', 'rt_dense_values'])

def ragged_range(starts: Any, limits: Any, deltas: Any, Tsplits: Any = ..., name: Optional[Any] = ...): ...

RaggedRange: Any

def ragged_range_eager_fallback(starts: Any, limits: Any, deltas: Any, Tsplits: Any, name: Any, ctx: Any): ...
