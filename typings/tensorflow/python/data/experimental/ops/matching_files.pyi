from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from typing import Any

class MatchingFilesDataset(dataset_ops.DatasetSource):
    def __init__(self, patterns: Any) -> None: ...
    @property
    def element_spec(self): ...
