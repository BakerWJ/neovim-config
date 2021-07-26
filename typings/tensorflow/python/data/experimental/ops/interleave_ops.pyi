from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import random_ops as random_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, readers as readers
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, gen_experimental_dataset_ops as gen_experimental_dataset_ops, gen_stateless_random_ops as gen_stateless_random_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def parallel_interleave(map_func: Any, cycle_length: Any, block_length: int = ..., sloppy: bool = ..., buffer_output_elements: Optional[Any] = ..., prefetch_input_elements: Optional[Any] = ...): ...

class _DirectedInterleaveDataset(dataset_ops.DatasetV2):
    def __init__(self, selector_input: Any, data_inputs: Any) -> None: ...
    @property
    def element_spec(self): ...

def sample_from_datasets_v2(datasets: Any, weights: Optional[Any] = ..., seed: Optional[Any] = ...): ...
def sample_from_datasets_v1(datasets: Any, weights: Optional[Any] = ..., seed: Optional[Any] = ...): ...
def choose_from_datasets_v2(datasets: Any, choice_dataset: Any): ...
def choose_from_datasets_v1(datasets: Any, choice_dataset: Any): ...
choose_from_datasets = choose_from_datasets_v2
sample_from_datasets = sample_from_datasets_v2
choose_from_datasets = choose_from_datasets_v1
sample_from_datasets = sample_from_datasets_v1
