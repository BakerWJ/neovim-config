import abc
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import cardinality as cardinality
from tensorflow.python.data.experimental.ops.distribute_options import AutoShardPolicy as AutoShardPolicy
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops, readers as readers
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor_utils as composite_tensor_utils, dtypes as dtypes, errors as errors, ops as ops, smart_cond as smart_cond, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.keras import losses as losses
from tensorflow.python.keras.utils import data_utils as data_utils, generic_utils as generic_utils, losses_utils as losses_utils
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.compat import collections_abc as collections_abc
from typing import Any, Optional

class Aggregator(metaclass=abc.ABCMeta):
    use_steps: Any = ...
    num_samples: Any = ...
    steps: Any = ...
    batch_size: Any = ...
    results: Any = ...
    def __init__(self, use_steps: Any, num_samples: Optional[Any] = ..., steps: Optional[Any] = ..., batch_size: Optional[Any] = ...) -> None: ...
    @abc.abstractmethod
    def create(self, batch_outs: Any) -> Any: ...
    @abc.abstractmethod
    def aggregate(self, batch_outs: Any, batch_start: Optional[Any] = ..., batch_end: Optional[Any] = ...) -> Any: ...
    @abc.abstractmethod
    def finalize(self) -> Any: ...

class MetricsAggregator(Aggregator):
    def __init__(self, use_steps: Any, num_samples: Optional[Any] = ..., steps: Optional[Any] = ...) -> None: ...
    results: Any = ...
    def create(self, batch_outs: Any) -> None: ...
    def aggregate(self, batch_outs: Any, batch_start: Optional[Any] = ..., batch_end: Optional[Any] = ...) -> None: ...
    def finalize(self) -> None: ...

class ConcatAggregator(Aggregator):
    composite: Any = ...
    def __init__(self, batch_size: Any) -> None: ...
    def create(self, batch_element: Any) -> None: ...
    def aggregate(self, batch_element: Any, batch_start: Optional[Any] = ..., batch_end: Optional[Any] = ...) -> None: ...
    results: Any = ...
    def finalize(self) -> None: ...

def get_copy_pool(): ...

class SliceAggregator(Aggregator):
    def __init__(self, num_samples: Any, batch_size: Any) -> None: ...
    results: Any = ...
    def create(self, batch_element: Any) -> None: ...
    def aggregate(self, batch_element: Any, batch_start: Any, batch_end: Any) -> None: ...
    def finalize(self) -> None: ...

class OutputsAggregator(Aggregator):
    def create(self, batch_outs: Any): ...
    def aggregate(self, batch_outs: Any, batch_start: Optional[Any] = ..., batch_end: Optional[Any] = ...) -> None: ...
    results: Any = ...
    def finalize(self) -> None: ...

def get_progbar(model: Any, count_mode: Any, include_metrics: bool = ...): ...
def slice_arrays(arrays: Any, indices: Any, contiguous: bool = ...): ...
def check_num_samples(ins: Any, batch_size: Optional[Any] = ..., steps: Optional[Any] = ..., steps_name: str = ...): ...
def standardize_single_array(x: Any, expected_shape: Optional[Any] = ...): ...
def standardize_input_data(data: Any, names: Any, shapes: Optional[Any] = ..., check_batch_axis: bool = ..., exception_prefix: str = ...): ...
def standardize_sample_or_class_weights(x_weight: Any, output_names: Any, weight_type: Any): ...
def standardize_class_weights(class_weight: Any, output_names: Any): ...
def standardize_sample_weights(sample_weight: Any, output_names: Any): ...
def handle_partial_sample_weights(outputs: Any, sample_weights: Any, sample_weight_modes: Any, check_all_flat: bool = ...): ...
def check_array_lengths(inputs: Any, targets: Any, weights: Optional[Any] = ...): ...
def check_loss_and_target_compatibility(targets: Any, loss_fns: Any, output_shapes: Any) -> None: ...
def collect_per_output_metric_info(metrics: Any, output_names: Any, output_shapes: Any, loss_fns: Any, is_weighted: bool = ...): ...
def batch_shuffle(index_array: Any, batch_size: Any): ...
def standardize_weights(y: Any, sample_weight: Optional[Any] = ..., class_weight: Optional[Any] = ..., sample_weight_mode: Optional[Any] = ...): ...
def has_symbolic_tensors(ls: Any): ...
def has_tensors(ls: Any): ...
def get_metric_name(metric: Any, weighted: bool = ...): ...
def get_metric_function(metric: Any, output_shape: Optional[Any] = ..., loss_fn: Optional[Any] = ...): ...
def call_metric_function(metric_fn: Any, y_true: Any, y_pred: Optional[Any] = ..., weights: Optional[Any] = ..., mask: Optional[Any] = ...): ...
def get_loss_function(loss: Any): ...

class RespectCompiledTrainableState:
    def __init__(self, model: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_arg: Any, value_arg: Any, traceback_arg: Any): ...

def validate_dataset_input(x: Any, y: Any, sample_weight: Any, validation_split: Optional[Any] = ...) -> None: ...
def validate_input_types(inp: Any, orig_inp: Any, allow_dict: bool = ..., field_name: str = ...) -> None: ...
def check_generator_arguments(y: Optional[Any] = ..., sample_weight: Optional[Any] = ..., validation_split: Optional[Any] = ...) -> None: ...
def check_steps_argument(input_data: Any, steps: Any, steps_name: Any): ...
def cast_single_tensor(x: Any, dtype: Optional[Any] = ...): ...
def cast_if_floating_dtype_and_mismatch(targets: Any, outputs: Any): ...
def cast_if_floating_dtype(x: Any, dtype: Optional[Any] = ...): ...
def cast_to_model_input_dtypes(x: Any, model: Any): ...
def prepare_sample_weight_modes(training_endpoints: Any, sample_weight_mode: Any) -> None: ...
def prepare_loss_functions(loss: Any, output_names: Any): ...
def prepare_loss_weights(training_endpoints: Any, loss_weights: Optional[Any] = ...) -> None: ...
def is_feature_layer(layer: Any): ...
def is_eager_dataset_or_iterator(data: Any): ...
def assert_not_batched(dataset: Any): ...
def assert_not_shuffled(dataset: Any): ...
def verify_dataset_shuffled(x: Any) -> None: ...
def is_dataset_or_iterator(data: Any): ...
def get_iterator(dataset: Any): ...
def initialize_iterator(iterator: Any) -> None: ...
def extract_tensors_from_dataset(dataset: Any): ...
def unpack_iterator_input(iterator: Any): ...
def infer_steps_for_dataset(model: Any, dataset: Any, steps: Any, epochs: int = ..., steps_name: str = ...): ...

class ModelInputs:
    def __init__(self, inputs: Any) -> None: ...
    def get_input_names(self): ...
    def get_symbolic_inputs(self, return_single_as_list: bool = ...): ...
    def as_dict(self) -> None: ...
    def as_list(self): ...

def get_input_shape_and_dtype(layer: Any): ...
def get_static_batch_size(layer: Any): ...
def generic_output_names(outputs_list: Any): ...
def convert_eager_tensors_to_numpy(structure: Any): ...
def list_to_tuple(maybe_list: Any): ...
def should_run_validation(validation_freq: Any, epoch: Any): ...
def split_training_and_validation_data(x: Any, y: Any, sample_weights: Any, validation_split: Any): ...
def unpack_validation_data(validation_data: Any, raise_if_ambiguous: bool = ...): ...

class TrainingLoop:
    def fit(self, model: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., batch_size: Optional[Any] = ..., epochs: int = ..., verbose: int = ..., callbacks: Optional[Any] = ..., validation_split: float = ..., validation_data: Optional[Any] = ..., shuffle: bool = ..., class_weight: Optional[Any] = ..., sample_weight: Optional[Any] = ..., initial_epoch: int = ..., steps_per_epoch: Optional[Any] = ..., validation_steps: Optional[Any] = ..., validation_freq: int = ..., **kwargs: Any) -> None: ...
    def evaluate(self, model: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., batch_size: Optional[Any] = ..., verbose: int = ..., sample_weight: Optional[Any] = ..., steps: Optional[Any] = ..., callbacks: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def predict(self, model: Any, x: Any, batch_size: Optional[Any] = ..., verbose: int = ..., steps: Optional[Any] = ..., callbacks: Optional[Any] = ..., **kwargs: Any) -> None: ...
