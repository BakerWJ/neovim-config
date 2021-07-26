from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.core.util import test_log_pb2 as test_log_pb2
from tensorflow.python.client import timeline as timeline
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import app as app, gfile as gfile
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

GLOBAL_BENCHMARK_REGISTRY: Any
TEST_REPORTER_TEST_ENV: str
OVERRIDE_GLOBAL_THREADPOOL: str

class _BenchmarkRegistrar(type):
    def __new__(mcs: Any, clsname: Any, base: Any, attrs: Any): ...

class ParameterizedBenchmark(_BenchmarkRegistrar):
    def __new__(mcs: Any, clsname: Any, base: Any, attrs: Any): ...

class Benchmark:
    @classmethod
    def is_abstract(cls): ...
    def report_benchmark(self, iters: Optional[Any] = ..., cpu_time: Optional[Any] = ..., wall_time: Optional[Any] = ..., throughput: Optional[Any] = ..., extras: Optional[Any] = ..., name: Optional[Any] = ..., metrics: Optional[Any] = ...) -> None: ...

def benchmark_config(): ...

class TensorFlowBenchmark(Benchmark):
    def __init__(self) -> None: ...
    @classmethod
    def is_abstract(cls): ...
    def run_op_benchmark(self, sess: Any, op_or_tensor: Any, feed_dict: Optional[Any] = ..., burn_iters: int = ..., min_iters: int = ..., store_trace: bool = ..., store_memory_usage: bool = ..., name: Optional[Any] = ..., extras: Optional[Any] = ..., mbs: int = ...): ...
    def evaluate(self, tensors: Any): ...

def benchmarks_main(true_main: Any, argv: Optional[Any] = ...): ...
