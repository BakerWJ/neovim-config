from tensorflow.python.compat import compat as compat
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, image_ops as image_ops, math_ops as math_ops, stateful_random_ops as stateful_random_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

ResizeMethod = image_ops.ResizeMethod

class Resizing(Layer):
    target_height: Any = ...
    target_width: Any = ...
    interpolation: Any = ...
    input_spec: Any = ...
    def __init__(self, height: Any, width: Any, interpolation: str = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    built: bool = ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class CenterCrop(Layer):
    target_height: Any = ...
    target_width: Any = ...
    input_spec: Any = ...
    def __init__(self, height: Any, width: Any, name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    built: bool = ...
    def build(self, input_shape: Any) -> None: ...
    def call(self, inputs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class RandomCrop(Layer):
    height: Any = ...
    width: Any = ...
    seed: Any = ...
    input_spec: Any = ...
    def __init__(self, height: Any, width: Any, seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class Rescaling(Layer):
    scale: Any = ...
    def __init__(self, scale: Any, name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

HORIZONTAL: str
VERTICAL: str
HORIZONTAL_AND_VERTICAL: str

class RandomFlip(Layer):
    mode: Any = ...
    horizontal: bool = ...
    vertical: bool = ...
    seed: Any = ...
    input_spec: Any = ...
    def __init__(self, mode: Any = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class RandomTranslation(Layer):
    height_factor: Any = ...
    height_lower: Any = ...
    height_upper: Any = ...
    width_factor: Any = ...
    width_lower: Any = ...
    width_upper: Any = ...
    fill_mode: Any = ...
    interpolation: Any = ...
    seed: Any = ...
    input_spec: Any = ...
    def __init__(self, height_factor: Any, width_factor: Any, fill_mode: str = ..., interpolation: str = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

def get_translation_matrix(translations: Any, name: Optional[Any] = ...): ...
def transform(images: Any, transforms: Any, fill_mode: str = ..., interpolation: str = ..., output_shape: Optional[Any] = ..., name: Optional[Any] = ...): ...
def get_rotation_matrix(angles: Any, image_height: Any, image_width: Any, name: Optional[Any] = ...): ...

class RandomRotation(Layer):
    factor: Any = ...
    lower: Any = ...
    upper: Any = ...
    fill_mode: Any = ...
    interpolation: Any = ...
    seed: Any = ...
    input_spec: Any = ...
    def __init__(self, factor: Any, fill_mode: str = ..., interpolation: str = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class RandomZoom(Layer):
    height_factor: Any = ...
    height_lower: Any = ...
    height_upper: Any = ...
    width_factor: Any = ...
    width_lower: Any = ...
    width_upper: Any = ...
    fill_mode: Any = ...
    interpolation: Any = ...
    seed: Any = ...
    input_spec: Any = ...
    def __init__(self, height_factor: Any, width_factor: Any, fill_mode: str = ..., interpolation: str = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

def get_zoom_matrix(zooms: Any, image_height: Any, image_width: Any, name: Optional[Any] = ...): ...

class RandomContrast(Layer):
    factor: Any = ...
    lower: Any = ...
    upper: Any = ...
    seed: Any = ...
    input_spec: Any = ...
    def __init__(self, factor: Any, seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class RandomHeight(Layer):
    factor: Any = ...
    height_lower: Any = ...
    height_upper: Any = ...
    interpolation: Any = ...
    input_spec: Any = ...
    seed: Any = ...
    def __init__(self, factor: Any, interpolation: str = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

class RandomWidth(Layer):
    factor: Any = ...
    width_lower: Any = ...
    width_upper: Any = ...
    interpolation: Any = ...
    input_spec: Any = ...
    seed: Any = ...
    def __init__(self, factor: Any, interpolation: str = ..., seed: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, inputs: Any, training: Optional[Any] = ...): ...
    def compute_output_shape(self, input_shape: Any): ...
    def get_config(self): ...

def make_generator(seed: Optional[Any] = ...): ...
def get_interpolation(interpolation: Any): ...
