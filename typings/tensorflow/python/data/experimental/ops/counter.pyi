from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import scan_ops as scan_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def CounterV2(start: int = ..., step: int = ..., dtype: Any = ...): ...
def CounterV1(start: int = ..., step: int = ..., dtype: Any = ...): ...
Counter = CounterV2
Counter = CounterV1
