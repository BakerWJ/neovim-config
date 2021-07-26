from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import random_seed as random_seed
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _ShuffleAndRepeatDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, buffer_size: Any, count: Optional[Any] = ..., seed: Optional[Any] = ...) -> None: ...

def shuffle_and_repeat(buffer_size: Any, count: Optional[Any] = ..., seed: Optional[Any] = ...): ...
