import abc
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.compat import compat as compat
from tensorflow.python.data.experimental.ops import distribute_options as distribute_options, optimization_options as optimization_options, stats_options as stats_options, threading_options as threading_options
from tensorflow.python.data.ops import iterator_ops as iterator_ops
from tensorflow.python.data.util import nest as nest, options as options_lib, random_seed as random_seed, structure as structure, traverse as traverse
from tensorflow.python.eager import context as context
from tensorflow.python.framework import auto_control_deps as auto_control_deps, composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, function as function, ops as ops, smart_cond as smart_cond, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_dataset_ops as gen_dataset_ops, gen_io_ops as gen_io_ops, math_ops as math_ops, script_ops as script_ops, string_ops as string_ops
from tensorflow.python.training.tracking import base as tracking_base, tracking as tracking
from tensorflow.python.util import deprecation as deprecation, function_utils as function_utils, lazy_loader as lazy_loader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

wrap_function: Any
autograph_ctx: Any
autograph: Any
AUTOTUNE: int

class DatasetV2(tracking_base.Trackable, composite_tensor.CompositeTensor, metaclass=abc.ABCMeta):
    def __init__(self, variant_tensor: Any): ...
    def options(self): ...
    def __iter__(self) -> Any: ...
    @property
    @abc.abstractmethod
    def element_spec(self) -> Any: ...
    def as_numpy_iterator(self): ...
    @staticmethod
    def from_tensors(tensors: Any): ...
    @staticmethod
    def from_tensor_slices(tensors: Any): ...
    class _GeneratorState:
        def __init__(self, generator: Any) -> None: ...
        def get_next_id(self, *args: Any): ...
        def get_iterator(self, iterator_id: Any): ...
        def iterator_completed(self, iterator_id: Any) -> None: ...
    @staticmethod
    def from_generator(generator: Any, output_types: Any, output_shapes: Optional[Any] = ..., args: Optional[Any] = ...): ...
    @staticmethod
    def range(*args: Any, **kwargs: Any): ...
    @staticmethod
    def zip(datasets: Any): ...
    def concatenate(self, dataset: Any): ...
    def prefetch(self, buffer_size: Any): ...
    @staticmethod
    def list_files(file_pattern: Any, shuffle: Optional[Any] = ..., seed: Optional[Any] = ...): ...
    def repeat(self, count: Optional[Any] = ...): ...
    def enumerate(self, start: int = ...): ...
    def shuffle(self, buffer_size: Any, seed: Optional[Any] = ..., reshuffle_each_iteration: Optional[Any] = ...): ...
    def cache(self, filename: str = ...): ...
    def take(self, count: Any): ...
    def skip(self, count: Any): ...
    def shard(self, num_shards: Any, index: Any): ...
    def batch(self, batch_size: Any, drop_remainder: bool = ...): ...
    def padded_batch(self, batch_size: Any, padded_shapes: Optional[Any] = ..., padding_values: Optional[Any] = ..., drop_remainder: bool = ...): ...
    def map(self, map_func: Any, num_parallel_calls: Optional[Any] = ..., deterministic: Optional[Any] = ...): ...
    def flat_map(self, map_func: Any): ...
    def interleave(self, map_func: Any, cycle_length: Any = ..., block_length: int = ..., num_parallel_calls: Optional[Any] = ..., deterministic: Optional[Any] = ...): ...
    def filter(self, predicate: Any): ...
    def apply(self, transformation_func: Any): ...
    def window(self, size: Any, shift: Optional[Any] = ..., stride: int = ..., drop_remainder: bool = ...): ...
    def reduce(self, initial_state: Any, reduce_func: Any): ...
    def unbatch(self): ...
    def with_options(self, options: Any): ...

class DatasetV1(DatasetV2, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    def make_one_shot_iterator(self): ...
    def make_initializable_iterator(self, shared_name: Optional[Any] = ...): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def element_spec(self): ...
    @staticmethod
    def from_tensors(tensors: Any): ...
    @staticmethod
    def from_tensor_slices(tensors: Any): ...
    @staticmethod
    def from_sparse_tensor_slices(sparse_tensor: Any): ...
    @staticmethod
    def from_generator(generator: Any, output_types: Any, output_shapes: Optional[Any] = ..., args: Optional[Any] = ...): ...
    @staticmethod
    def range(*args: Any, **kwargs: Any): ...
    @staticmethod
    def zip(datasets: Any): ...
    def concatenate(self, dataset: Any): ...
    def prefetch(self, buffer_size: Any): ...
    @staticmethod
    def list_files(file_pattern: Any, shuffle: Optional[Any] = ..., seed: Optional[Any] = ...): ...
    def repeat(self, count: Optional[Any] = ...): ...
    def shuffle(self, buffer_size: Any, seed: Optional[Any] = ..., reshuffle_each_iteration: Optional[Any] = ...): ...
    def cache(self, filename: str = ...): ...
    def take(self, count: Any): ...
    def skip(self, count: Any): ...
    def shard(self, num_shards: Any, index: Any): ...
    def batch(self, batch_size: Any, drop_remainder: bool = ...): ...
    def padded_batch(self, batch_size: Any, padded_shapes: Optional[Any] = ..., padding_values: Optional[Any] = ..., drop_remainder: bool = ...): ...
    def map(self, map_func: Any, num_parallel_calls: Optional[Any] = ..., deterministic: Optional[Any] = ...): ...
    def map_with_legacy_function(self, map_func: Any, num_parallel_calls: Optional[Any] = ..., deterministic: Optional[Any] = ...): ...
    def flat_map(self, map_func: Any): ...
    def interleave(self, map_func: Any, cycle_length: Any = ..., block_length: int = ..., num_parallel_calls: Optional[Any] = ..., deterministic: Optional[Any] = ...): ...
    def filter(self, predicate: Any): ...
    def filter_with_legacy_function(self, predicate: Any): ...
    def apply(self, transformation_func: Any): ...
    def window(self, size: Any, shift: Optional[Any] = ..., stride: int = ..., drop_remainder: bool = ...): ...
    def unbatch(self): ...
    def with_options(self, options: Any): ...
Dataset = DatasetV2
Dataset = DatasetV1

class DatasetV1Adapter(DatasetV1):
    def __init__(self, dataset: Any) -> None: ...
    def options(self): ...
    @property
    def element_spec(self): ...
    def __iter__(self) -> Any: ...

def make_one_shot_iterator(dataset: Any): ...
def make_initializable_iterator(dataset: Any, shared_name: Optional[Any] = ...): ...
def get_structure(dataset_or_iterator: Any): ...
def get_legacy_output_classes(dataset_or_iterator: Any): ...
def get_legacy_output_shapes(dataset_or_iterator: Any): ...
def get_legacy_output_types(dataset_or_iterator: Any): ...

class Options(options_lib.OptionsBase):
    experimental_deterministic: Any = ...
    experimental_distribute: Any = ...
    experimental_optimization: Any = ...
    experimental_slack: Any = ...
    experimental_stats: Any = ...
    experimental_threading: Any = ...
    experimental_external_state_policy: Any = ...
    def merge(self, options: Any): ...

class DatasetSource(DatasetV2, metaclass=abc.ABCMeta): ...

class UnaryDataset(DatasetV2, metaclass=abc.ABCMeta):
    def __init__(self, input_dataset: Any, variant_tensor: Any) -> None: ...

class UnaryUnchangedStructureDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, variant_tensor: Any) -> None: ...
    @property
    def element_spec(self): ...

class TensorDataset(DatasetSource):
    def __init__(self, element: Any) -> None: ...
    @property
    def element_spec(self): ...

class TensorSliceDataset(DatasetSource):
    def __init__(self, element: Any): ...
    @property
    def element_spec(self): ...

class SparseTensorSliceDataset(DatasetSource):
    def __init__(self, sparse_tensor: Any) -> None: ...
    @property
    def element_spec(self): ...

class _VariantDataset(DatasetV2):
    def __init__(self, dataset_variant: Any, structure: Any) -> None: ...
    @property
    def element_spec(self): ...

class _NestedVariant(composite_tensor.CompositeTensor):
    def __init__(self, variant_tensor: Any, element_spec: Any, dataset_shape: Any) -> None: ...

def from_variant(variant: Any, structure: Any): ...
def to_variant(dataset: Any): ...

class DatasetSpec(type_spec.BatchableTypeSpec):
    def __init__(self, element_spec: Any, dataset_shape: Any = ...) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value: Any): ...

class StructuredFunctionWrapper:
    def __init__(self, func: Any, transformation_name: Any, dataset: Optional[Any] = ..., input_classes: Optional[Any] = ..., input_shapes: Optional[Any] = ..., input_types: Optional[Any] = ..., input_structure: Optional[Any] = ..., add_to_graph: bool = ..., use_legacy_function: bool = ..., defun_kwargs: Optional[Any] = ...): ...
    @property
    def output_structure(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def function(self): ...

class _GeneratorDataset(DatasetSource):
    def __init__(self, init_args: Any, init_func: Any, next_func: Any, finalize_func: Any) -> None: ...
    @property
    def element_spec(self): ...

class ZipDataset(DatasetV2):
    def __init__(self, datasets: Any) -> None: ...
    @property
    def element_spec(self): ...

class ConcatenateDataset(DatasetV2):
    def __init__(self, input_dataset: Any, dataset_to_concatenate: Any) -> None: ...
    @property
    def element_spec(self): ...

class RepeatDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, count: Any) -> None: ...

class RangeDataset(DatasetSource):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def element_spec(self): ...

class _MemoryCacheDeleter:
    def __init__(self, handle: Any, device: Any, deleter: Any) -> None: ...
    def __del__(self) -> None: ...

class _MemoryCache:
    def __init__(self) -> None: ...
    @property
    def handle(self): ...

class CacheDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, filename: Any) -> None: ...

class _RandomSeedGeneratorDeleter:
    def __init__(self, handle: Any, device: Any, deleter: Any) -> None: ...
    def __del__(self) -> None: ...

class _RandomSeedGenerator:
    def __init__(self, seed: Any, seed2: Any) -> None: ...
    @property
    def handle(self): ...

class ShuffleDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, buffer_size: Any, seed: Optional[Any] = ..., reshuffle_each_iteration: Optional[Any] = ...) -> None: ...

class TakeDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, count: Any) -> None: ...

class SkipDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, count: Any) -> None: ...

class ShardDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, num_shards: Any, index: Any) -> None: ...

class BatchDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, batch_size: Any, drop_remainder: Any): ...
    @property
    def element_spec(self): ...

class _NumpyIterator:
    def __init__(self, dataset: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def next(self): ...
    def __next__(self): ...

class _VariantTracker(tracking.CapturableResource):
    def __init__(self, variant_tensor: Any, resource_creator: Any) -> None: ...

class PaddedBatchDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, batch_size: Any, padded_shapes: Any, padding_values: Any, drop_remainder: Any): ...
    @property
    def element_spec(self): ...

class MapDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, map_func: Any, use_inter_op_parallelism: bool = ..., preserve_cardinality: bool = ..., use_legacy_function: bool = ...) -> None: ...
    @property
    def element_spec(self): ...

class ParallelMapDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, map_func: Any, num_parallel_calls: Any, deterministic: Any, use_inter_op_parallelism: bool = ..., preserve_cardinality: bool = ..., use_legacy_function: bool = ...) -> None: ...
    @property
    def element_spec(self): ...

class FlatMapDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, map_func: Any) -> None: ...
    @property
    def element_spec(self): ...

class InterleaveDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, map_func: Any, cycle_length: Any, block_length: Any) -> None: ...
    @property
    def element_spec(self): ...

class ParallelInterleaveDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, map_func: Any, cycle_length: Any, block_length: Any, num_parallel_calls: Any, buffer_output_elements: Any = ..., prefetch_input_elements: Any = ..., deterministic: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class FilterDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, predicate: Any, use_legacy_function: bool = ...) -> None: ...

class PrefetchDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, buffer_size: Any, slack_period: Optional[Any] = ...) -> None: ...

class WindowDataset(UnaryDataset):
    def __init__(self, input_dataset: Any, size: Any, shift: Any, stride: Any, drop_remainder: Any) -> None: ...
    @property
    def element_spec(self): ...

class _OptionsDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, options: Any) -> None: ...
    def options(self): ...

class _ModelDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, algorithm: Any, cpu_budget: Any) -> None: ...

class _OptimizeDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, optimizations: Any, optimization_configs: Optional[Any] = ...) -> None: ...

class _SetStatsAggregatorDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, aggregator: Any, prefix: Any, counter_prefix: Any) -> None: ...

class _MaxIntraOpParallelismDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, max_intra_op_parallelism: Any) -> None: ...

class _PrivateThreadPoolDataset(UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, num_threads: Any) -> None: ...

def normalize_to_dense(dataset: Any): ...

class _RestructuredDataset(UnaryDataset):
    def __init__(self, dataset: Any, structure: Any) -> None: ...
    @property
    def element_spec(self): ...

class _UnbatchDataset(UnaryDataset):
    def __init__(self, input_dataset: Any): ...
    @property
    def element_spec(self): ...