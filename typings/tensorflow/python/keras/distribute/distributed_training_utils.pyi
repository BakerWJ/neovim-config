from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.distribute import multi_worker_util as multi_worker_util, reduce_util as reduce_util
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.keras import callbacks as callbacks, optimizers as optimizers
from tensorflow.python.keras.engine import training_utils as training_utils
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops, sparse_ops as sparse_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_concat_ops as ragged_concat_ops, ragged_tensor as ragged_tensor
from tensorflow.python.util import nest as nest, tf_contextlib as tf_contextlib
from typing import Any, Optional

def set_weights(distribution_strategy: Any, dist_model: Any, weights: Any) -> None: ...
def unwrap_values(distribution_strategy: Any, grouped_inputs: Any, grouped_outputs: Any, grouped_updates: Optional[Any] = ..., grouped_session_args: Optional[Any] = ..., with_loss_tensor: bool = ...): ...
def unwrap_output_dict(strategy: Any, grouped_outputs: Any, mode: Any): ...
def unwrap_outputs(distribution_strategy: Any, grouped_outputs: Any, with_loss_tensor: bool = ...): ...
def flatten_per_replica_values(distribution_strategy: Any, per_replica_values: Any): ...
def validate_callbacks(input_callbacks: Any, optimizer: Any) -> None: ...
def validate_distributed_dataset_inputs(distribution_strategy: Any, x: Any, y: Any, sample_weights: Optional[Any] = ...): ...
def validate_per_replica_inputs(distribution_strategy: Any, x: Any): ...
def validate_all_tensor_types(x: Any, x_values: Any) -> None: ...
def validate_all_tensor_shapes(x: Any, x_values: Any) -> None: ...
def init_restore_or_wait_for_variables() -> None: ...
def validate_inputs(x: Any, y: Any) -> None: ...
def global_batch_size_supported(distribution_strategy: Any): ...
def is_tpu_strategy(strategy: Any): ...
def is_dataset_shape_fully_defined(dataset: Any): ...
def process_batch_and_step_size(strategy: Any, inputs: Any, batch_size: Any, steps_per_epoch: Any, mode: Any, validation_split: float = ...): ...
def get_input_params(distribution_strategy: Any, num_samples: Any, steps: Any, batch_size: Any, mode: Optional[Any] = ...): ...
def get_batch_dimension(iterator: Any): ...
def get_iterator(dataset: Any, distribution_strategy: Any): ...
def initialize_iterator(iterator: Any, distribution_strategy: Any) -> None: ...
def is_distributing_by_cloning(model: Any): ...
def clone_model_on_replicas(model: Any, strategy: Any, mode: Any, inputs: Optional[Any] = ..., targets: Optional[Any] = ...) -> None: ...
def get_distributed_model(model: Any, mode: Any): ...
def set_distributed_model(model: Any, mode: Any, distributed_model: Any) -> None: ...
def get_distributed_function(model: Any, mode: Any): ...
def set_distributed_function(model: Any, mode: Any, distributed_function: Any) -> None: ...
def distributed_scope(strategy: Any, learning_phase: Any) -> None: ...
def call_replica_local_fn(fn: Any, *args: Any, **kwargs: Any): ...
def is_current_worker_chief(): ...
def filter_distributed_callbacks(callbacks_list: Any, model: Any): ...
def concat_along_batch_dimension(outputs: Any): ...
