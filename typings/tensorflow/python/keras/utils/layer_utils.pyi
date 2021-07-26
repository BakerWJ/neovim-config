from tensorflow.python.keras.utils.conv_utils import convert_kernel as convert_kernel
from tensorflow.python.util import deprecation as deprecation, nest as nest, object_identity as object_identity
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

def get_source_inputs(tensor: Any, layer: Optional[Any] = ..., node_index: Optional[Any] = ...): ...
def validate_string_arg(input_data: Any, allowable_strings: Any, layer_name: Any, arg_name: Any, allow_none: bool = ..., allow_callables: bool = ...) -> None: ...
def count_params(weights: Any): ...
def print_summary(model: Any, line_length: Optional[Any] = ..., positions: Optional[Any] = ..., print_fn: Optional[Any] = ...) -> None: ...
def gather_trainable_weights(trainable: Any, sub_layers: Any, extra_variables: Any): ...
def gather_non_trainable_weights(trainable: Any, sub_layers: Any, extra_variables: Any): ...
def convert_all_kernels_in_model(model: Any) -> None: ...
def convert_dense_weights_data_format(dense: Any, previous_feature_map_shape: Any, target_data_format: str = ...) -> None: ...
def is_builtin_layer(layer: Any): ...
