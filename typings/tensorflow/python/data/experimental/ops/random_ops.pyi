from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import random_seed as random_seed
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class RandomDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, seed: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class RandomDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, seed: Optional[Any] = ...) -> None: ...
RandomDataset = RandomDatasetV2
RandomDataset = RandomDatasetV1
