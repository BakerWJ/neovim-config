from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _ScanDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, initial_state: Any, scan_func: Any, use_default_device: Optional[Any] = ...): ...
    @property
    def element_spec(self): ...

def scan(initial_state: Any, scan_func: Any): ...
