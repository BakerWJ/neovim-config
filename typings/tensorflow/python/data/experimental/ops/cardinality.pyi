from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

INFINITE: int
UNKNOWN: int

def cardinality(dataset: Any): ...
def assert_cardinality(expected_cardinality: Any): ...

class _AssertCardinalityDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, expected_cardinality: Any) -> None: ...
