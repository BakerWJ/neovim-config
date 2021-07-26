from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import structure as structure
from tensorflow.python.framework import dtypes as dtypes, sparse_tensor as sparse_tensor, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops, parsing_ops as parsing_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _ParseExampleDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, features: Any, num_parallel_calls: Any, deterministic: Any) -> None: ...
    @property
    def element_spec(self): ...

def parse_example_dataset(features: Any, num_parallel_calls: int = ..., deterministic: Optional[Any] = ...): ...
