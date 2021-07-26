from collections import namedtuple
from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.framework import c_api_util as c_api_util
from tensorflow.python.util import compat as compat
from typing import Any

_MetricMethod = namedtuple('MetricMethod', 'create delete get_cell')

class Metric:
    def __init__(self, metric_name: Any, metric_methods: Any, label_length: Any, *args: Any) -> None: ...
    def __del__(self) -> None: ...
    def get_cell(self, *labels: Any): ...

class CounterCell:
    def __init__(self, cell: Any) -> None: ...
    def increase_by(self, value: Any) -> None: ...
    def value(self): ...

class Counter(Metric):
    def __init__(self, name: Any, description: Any, *labels: Any) -> None: ...
    def get_cell(self, *labels: Any): ...

class IntGaugeCell:
    def __init__(self, cell: Any) -> None: ...
    def set(self, value: Any) -> None: ...
    def value(self): ...

class IntGauge(Metric):
    def __init__(self, name: Any, description: Any, *labels: Any) -> None: ...
    def get_cell(self, *labels: Any): ...

class StringGaugeCell:
    def __init__(self, cell: Any) -> None: ...
    def set(self, value: Any) -> None: ...
    def value(self): ...

class StringGauge(Metric):
    def __init__(self, name: Any, description: Any, *labels: Any) -> None: ...
    def get_cell(self, *labels: Any): ...

class BoolGaugeCell:
    def __init__(self, cell: Any) -> None: ...
    def set(self, value: Any) -> None: ...
    def value(self): ...

class BoolGauge(Metric):
    def __init__(self, name: Any, description: Any, *labels: Any) -> None: ...
    def get_cell(self, *labels: Any): ...

class SamplerCell:
    def __init__(self, cell: Any) -> None: ...
    def add(self, value: Any) -> None: ...
    def value(self): ...

class Buckets:
    buckets: Any = ...
    def __init__(self, buckets: Any) -> None: ...
    def __del__(self) -> None: ...

class ExponentialBuckets(Buckets):
    def __init__(self, scale: Any, growth_factor: Any, bucket_count: Any) -> None: ...

class Sampler(Metric):
    def __init__(self, name: Any, buckets: Any, description: Any, *labels: Any) -> None: ...
    def get_cell(self, *labels: Any): ...
