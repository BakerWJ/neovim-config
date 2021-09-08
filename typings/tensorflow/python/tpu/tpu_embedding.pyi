from collections import namedtuple
from tensorflow.core.protobuf.tpu import optimization_parameters_pb2 as optimization_parameters_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, partitioned_variables as partitioned_variables, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

TRAINING: Any
INFERENCE: Any

class TableConfig:
    def __new__(cls, vocabulary_size: Any, dimension: Any, initializer: Optional[Any] = ..., combiner: str = ..., hot_id_replication: bool = ..., learning_rate: Optional[Any] = ..., learning_rate_fn: Optional[Any] = ...): ...

class FeatureConfig:
    def __new__(cls, table_id: Any, max_sequence_length: int = ..., weight_key: Optional[Any] = ...): ...

class EnqueueData:
    def __new__(cls, embedding_indices: Any, sample_indices: Optional[Any] = ..., aggregation_weights: Optional[Any] = ...): ...
    @staticmethod
    def from_sparse_tensor(sp_tensor: Any, weights: Optional[Any] = ...): ...

def get_enqueue_datas_list_from_sparse_tensors_list(sp_tensors_list: Any): ...

AdamSlotVariableNames = namedtuple('AdamSlotVariableNames', ['m', 'v'])

AdagradSlotVariableName = namedtuple('AdagradSlotVariableName', ['accumulator'])

FtrlSlotVariableName = namedtuple('FtrlSlotVariableName', ['accumulator', 'linear'])

AdamSlotVariables = namedtuple('AdamSlotVariables', ['m', 'v'])

AdagradSlotVariable = namedtuple('AdagradSlotVariable', ['accumulator'])

FtrlSlotVariable = namedtuple('FtrlSlotVariable', ['accumulator', 'linear'])

VariablesAndOps = namedtuple('VariablesAndOps', ['embedding_variables_by_table', 'slot_variables_by_table', 'load_ops', 'retrieve_ops'])

class _OptimizationParameters:
    learning_rate: Any = ...
    use_gradient_accumulation: Any = ...
    clip_weight_min: Any = ...
    clip_weight_max: Any = ...
    weight_decay_factor: Any = ...
    multiply_weight_decay_factor_by_learning_rate: Any = ...
    def __init__(self, learning_rate: Any, use_gradient_accumulation: Any, clip_weight_min: Any, clip_weight_max: Any, weight_decay_factor: Any, multiply_weight_decay_factor_by_learning_rate: Any) -> None: ...

class AdagradParameters(_OptimizationParameters):
    initial_accumulator: Any = ...
    def __init__(self, learning_rate: Any, initial_accumulator: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[Any] = ..., clip_weight_max: Optional[Any] = ..., weight_decay_factor: Optional[Any] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[Any] = ...) -> None: ...

class AdamParameters(_OptimizationParameters):
    beta1: Any = ...
    beta2: Any = ...
    epsilon: Any = ...
    lazy_adam: Any = ...
    sum_inside_sqrt: Any = ...
    def __init__(self, learning_rate: Any, beta1: float = ..., beta2: float = ..., epsilon: float = ..., lazy_adam: bool = ..., sum_inside_sqrt: bool = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[Any] = ..., clip_weight_max: Optional[Any] = ..., weight_decay_factor: Optional[Any] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[Any] = ...) -> None: ...

class FtrlParameters(_OptimizationParameters):
    learning_rate_power: Any = ...
    initial_accumulator_value: Any = ...
    initial_linear_value: float = ...
    l1_regularization_strength: Any = ...
    l2_regularization_strength: Any = ...
    def __init__(self, learning_rate: Any, learning_rate_power: Any = ..., initial_accumulator_value: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[Any] = ..., clip_weight_max: Optional[Any] = ..., weight_decay_factor: Optional[Any] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[Any] = ...) -> None: ...

class StochasticGradientDescentParameters(_OptimizationParameters):
    def __init__(self, learning_rate: Any, clip_weight_min: Optional[Any] = ..., clip_weight_max: Optional[Any] = ..., weight_decay_factor: Optional[Any] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[Any] = ...) -> None: ...

DeviceConfig = namedtuple('DeviceConfig', ['num_hosts', 'num_cores', 'job_name'])

class TPUEmbedding:
    def __init__(self, table_to_config_dict: Any, feature_to_config_dict: Any, batch_size: Any, mode: Any, master: Optional[Any] = ..., optimization_parameters: Optional[Any] = ..., cluster_def: Optional[Any] = ..., pipeline_execution_with_tensor_core: bool = ..., partition_strategy: str = ..., device_config: Optional[Any] = ..., master_job_name: Optional[Any] = ...) -> None: ...
    @property
    def hosts(self): ...
    @property
    def num_cores_per_host(self): ...
    @property
    def num_cores(self): ...
    @property
    def batch_size_per_core(self): ...
    @property
    def config_proto(self): ...
    @property
    def table_to_config_dict(self): ...
    @property
    def feature_to_config_dict(self): ...
    @property
    def table_to_features_dict(self): ...
    @property
    def optimization_parameters(self): ...
    def create_variables_and_ops(self, embedding_variable_name_by_table: Optional[Any] = ..., slot_variable_names_by_table: Optional[Any] = ...): ...
    def generate_enqueue_ops(self, enqueue_datas_list: Any, mode_override: Optional[Any] = ...): ...
    def get_activations(self): ...
    def generate_send_gradients_op(self, feature_to_gradient_dict: Any, step: Optional[Any] = ...): ...

class _OptimizerHandler:
    def __init__(self, optimization_parameters: Any) -> None: ...
    def set_optimization_parameters(self, table_descriptor: Any) -> None: ...
    def get_default_slot_variable_names(self, table: Any) -> None: ...
    def create_variables_and_ops(self, table: Any, slot_variable_names: Any, num_hosts: Any, table_config: Any, table_variables: Any, config_proto: Any) -> None: ...

class _AdagradHandler(_OptimizerHandler):
    def __init__(self, optimization_parameters: Any) -> None: ...
    def set_optimization_parameters(self, table_descriptor: Any) -> None: ...
    def get_default_slot_variable_names(self, table: Any): ...
    def create_variables_and_ops(self, table: Any, slot_variable_names: Any, num_hosts: Any, table_config: Any, table_variables: Any, config_proto: Any): ...

class _AdamHandler(_OptimizerHandler):
    def __init__(self, optimization_parameters: Any) -> None: ...
    def set_optimization_parameters(self, table_descriptor: Any) -> None: ...
    def get_default_slot_variable_names(self, table: Any): ...
    def create_variables_and_ops(self, table: Any, slot_variable_names: Any, num_hosts: Any, table_config: Any, table_variables: Any, config_proto: Any): ...

class _FtrlHandler(_OptimizerHandler):
    def __init__(self, optimization_parameters: Any) -> None: ...
    def set_optimization_parameters(self, table_descriptor: Any) -> None: ...
    def get_default_slot_variable_names(self, table: Any): ...
    def create_variables_and_ops(self, table: Any, slot_variable_names: Any, num_hosts: Any, table_config: Any, table_variables: Any, config_proto: Any): ...

class _StochasticGradientDescentHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor: Any) -> None: ...
    def get_default_slot_variable_names(self, table: Any) -> None: ...
    def create_variables_and_ops(self, table: Any, slot_variable_names: Any, num_hosts: Any, table_config: Any, table_variables: Any, config_proto: Any): ...