from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class _TakeWhileDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, predicate: Any) -> None: ...

def take_while(predicate: Any): ...
