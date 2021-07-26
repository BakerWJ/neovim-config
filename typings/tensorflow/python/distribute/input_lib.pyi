from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import batching as batching, distribute as distribute
from tensorflow.python.data.ops import dataset_ops as dataset_ops, multi_device_iterator_ops as multi_device_iterator_ops
from tensorflow.python.distribute import device_util as device_util, distribution_strategy_context as distribution_strategy_context, input_ops as input_ops, reduce_util as reduce_util, values as values
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import nest as nest
from tensorflow.python.util.deprecation import deprecated as deprecated
from typing import Any, Optional

def get_distributed_dataset(dataset: Any, input_workers: Any, strategy: Any, split_batch_by: Optional[Any] = ..., input_context: Optional[Any] = ...): ...
def get_distributed_datasets_from_function(dataset_fn: Any, input_workers: Any, input_contexts: Any, strategy: Any): ...

class InputWorkers:
    def __init__(self, worker_device_pairs: Any) -> None: ...
    @property
    def num_workers(self): ...
    @property
    def worker_devices(self): ...
    def compute_devices_for_worker(self, worker_index: Any): ...
    def serialize(self): ...
    def deserialize(self, worker_device_pairs: Any): ...

class DistributedIteratorBase:
    def __init__(self, input_workers: Any, iterators: Any, strategy: Any) -> None: ...
    def next(self): ...
    def __next__(self): ...
    def __iter__(self) -> Any: ...
    def get_next(self, name: Optional[Any] = ...): ...

class DistributedIteratorV1(DistributedIteratorBase):
    def initialize(self): ...
    @property
    def initializer(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    def get_iterator(self, worker: Any): ...
    @property
    def element_spec(self): ...

class DistributedIteratorSpec(type_spec.TypeSpec):
    def __init__(self, input_workers: Any, element_spec: Any, strategy: Any) -> None: ...
    @property
    def value_type(self): ...
    def most_specific_compatible_type(self, other: Any): ...
    @staticmethod
    def from_value(value: Any): ...

class DistributedIterator(DistributedIteratorBase, composite_tensor.CompositeTensor):
    def __init__(self, input_workers: Optional[Any] = ..., iterators: Optional[Any] = ..., strategy: Optional[Any] = ..., components: Optional[Any] = ..., element_spec: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class _IterableInput:
    def __init__(self, input_workers: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def reduce(self, initial_state: Any, reduce_fn: Any): ...

class DistributedDataset(_IterableInput):
    def __init__(self, dataset: Any, input_workers: Any, strategy: Any, split_batch_by: Optional[Any] = ..., input_context: Optional[Any] = ...) -> None: ...
    def __iter__(self) -> Any: ...
    @property
    def element_spec(self): ...

class DistributedDatasetV1(DistributedDataset):
    def __init__(self, dataset: Any, input_workers: Any, strategy: Any, split_batch_by: Optional[Any] = ..., input_context: Optional[Any] = ...) -> None: ...
    def make_one_shot_iterator(self): ...
    def make_initializable_iterator(self): ...
    def __iter__(self) -> Any: ...

class DistributedDatasetsFromFunction(_IterableInput):
    def __init__(self, dataset_fn: Any, input_workers: Any, input_contexts: Any, strategy: Any) -> None: ...
    def __iter__(self) -> Any: ...
    @property
    def element_spec(self): ...

class DistributedDatasetsFromFunctionV1(DistributedDatasetsFromFunction):
    def __iter__(self) -> Any: ...

class InputFunctionIterator(DistributedIteratorV1):
    def __init__(self, input_fn: Any, input_workers: Any, input_contexts: Any, strategy: Any) -> None: ...

class DatasetIterator(DistributedIteratorV1):
    def __init__(self, dataset: Any, input_workers: Any, strategy: Any, split_batch_by: Optional[Any] = ..., input_context: Optional[Any] = ...) -> None: ...

class _SingleWorkerDatasetIteratorBase:
    def __init__(self, dataset: Any, worker: Any, devices: Any) -> None: ...
    def get_next(self, device: Any, name: Optional[Any] = ...): ...
    def get_next_as_list_static_shapes(self, name: Optional[Any] = ...): ...
    def get_next_as_list(self, name: Optional[Any] = ...): ...

class _SingleWorkerDatasetIteratorSpec(type_spec.TypeSpec):
    def __init__(self, worker: Any, devices: Any, element_spec: Any) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value: Any): ...

class _SingleWorkerOwnedDatasetIterator(_SingleWorkerDatasetIteratorBase, composite_tensor.CompositeTensor):
    def __init__(self, dataset: Optional[Any] = ..., worker: Optional[Any] = ..., devices: Optional[Any] = ..., components: Optional[Any] = ..., element_spec: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class _SingleWorkerDatasetIterator(_SingleWorkerDatasetIteratorBase):
    def initialize(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...

class _SingleWorkerCallableIterator:
    def __init__(self, fn: Any, worker: Any, devices: Any) -> None: ...
    def get_next(self, device: Any, name: Optional[Any] = ...): ...
    def get_next_as_list_static_shapes(self, name: Optional[Any] = ...): ...
    def get_next_as_list(self, name: Optional[Any] = ...): ...
    def initialize(self): ...

class MultiStepContext:
    def __init__(self) -> None: ...
    @property
    def last_step_outputs(self): ...
    def set_last_step_output(self, name: Any, output: Any, reduce_op: Optional[Any] = ...) -> None: ...
    @property
    def non_tensor_outputs(self): ...
    def set_non_tensor_output(self, name: Any, output: Any) -> None: ...
