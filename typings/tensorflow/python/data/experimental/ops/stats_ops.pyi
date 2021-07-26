from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def set_stats_aggregator(stats_aggregator: Any, prefix: str = ..., counter_prefix: str = ...): ...
def bytes_produced_stats(tag: Any): ...
def latency_stats(tag: Any): ...

class _StatsDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, op_function: Any, tag: Any) -> None: ...
