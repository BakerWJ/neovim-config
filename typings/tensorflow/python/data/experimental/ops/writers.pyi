from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class TFRecordWriter:
    def __init__(self, filename: Any, compression_type: Optional[Any] = ...) -> None: ...
    def write(self, dataset: Any): ...
