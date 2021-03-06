from tensorflow.python import keras as keras, tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import tensor_shape as tensor_shape, tensor_spec as tensor_spec, test_util as test_util
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.util import tf_contextlib as tf_contextlib, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import Any, Optional

def get_test_data(train_samples: Any, test_samples: Any, input_shape: Any, num_classes: Any, random_seed: Optional[Any] = ...): ...
def layer_test(layer_cls: Any, kwargs: Optional[Any] = ..., input_shape: Optional[Any] = ..., input_dtype: Optional[Any] = ..., input_data: Optional[Any] = ..., expected_output: Optional[Any] = ..., expected_output_dtype: Optional[Any] = ..., expected_output_shape: Optional[Any] = ..., validate_training: bool = ..., adapt_data: Optional[Any] = ...): ...
def model_type_scope(value: Any) -> None: ...
def run_eagerly_scope(value: Any) -> None: ...
def should_run_eagerly(): ...
def experimental_run_tf_function_scope(value: Any) -> None: ...
def should_run_tf_function(): ...
def saved_model_format_scope(value: Any) -> None: ...
def get_save_format(): ...
def get_model_type(): ...
def get_small_sequential_mlp(num_hidden: Any, num_classes: Any, input_dim: Optional[Any] = ...): ...
def get_small_functional_mlp(num_hidden: Any, num_classes: Any, input_dim: Any): ...

class SmallSubclassMLP(keras.Model):
    use_bn: Any = ...
    use_dp: Any = ...
    layer_a: Any = ...
    layer_b: Any = ...
    dp: Any = ...
    bn: Any = ...
    def __init__(self, num_hidden: Any, num_classes: Any, use_bn: bool = ..., use_dp: bool = ...) -> None: ...
    def call(self, inputs: Any, **kwargs: Any): ...

class _SmallSubclassMLPCustomBuild(keras.Model):
    layer_a: Any = ...
    layer_b: Any = ...
    num_hidden: Any = ...
    num_classes: Any = ...
    def __init__(self, num_hidden: Any, num_classes: Any) -> None: ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any, **kwargs: Any): ...

def get_small_subclass_mlp(num_hidden: Any, num_classes: Any): ...
def get_small_subclass_mlp_with_custom_build(num_hidden: Any, num_classes: Any): ...
def get_small_mlp(num_hidden: Any, num_classes: Any, input_dim: Any): ...

class _SubclassModel(keras.Model):
    num_layers: Any = ...
    def __init__(self, layers: Any, *args: Any, **kwargs: Any) -> None: ...
    def call(self, inputs: Any, **kwargs: Any): ...

class _SubclassModelCustomBuild(keras.Model):
    all_layers: Any = ...
    def __init__(self, layer_generating_func: Any, *args: Any, **kwargs: Any) -> None: ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any, **kwargs: Any): ...

def get_model_from_layers(layers: Any, input_shape: Optional[Any] = ..., input_dtype: Optional[Any] = ..., name: Optional[Any] = ..., input_ragged: Optional[Any] = ..., input_sparse: Optional[Any] = ...): ...

class Bias(keras.layers.Layer):
    bias: Any = ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any): ...

class _MultiIOSubclassModel(keras.Model):
    def __init__(self, branch_a: Any, branch_b: Any, shared_input_branch: Optional[Any] = ..., shared_output_branch: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def call(self, inputs: Any, **kwargs: Any): ...

class _MultiIOSubclassModelCustomBuild(keras.Model):
    def __init__(self, branch_a_func: Any, branch_b_func: Any, shared_input_branch_func: Optional[Any] = ..., shared_output_branch_func: Optional[Any] = ...) -> None: ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any, **kwargs: Any): ...

def get_multi_io_model(branch_a: Any, branch_b: Any, shared_input_branch: Optional[Any] = ..., shared_output_branch: Optional[Any] = ...): ...
def get_v2_optimizer(name: Any, **kwargs: Any): ...
def get_expected_metric_variable_names(var_names: Any, name_suffix: str = ...): ...
def enable_v2_dtype_behavior(fn: Any): ...
def disable_v2_dtype_behavior(fn: Any): ...
