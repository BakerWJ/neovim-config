from tensorflow.python.client import session as session
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.platform import test as test
from typing import Any, Optional

class DatasetBenchmarkBase(test.Benchmark):
    def run_benchmark(self, dataset: Any, num_elements: Any, iters: int = ..., warmup: bool = ...): ...
    def run_and_report_benchmark(self, dataset: Any, num_elements: Any, name: Any, iters: int = ..., extras: Optional[Any] = ..., warmup: bool = ...) -> None: ...
