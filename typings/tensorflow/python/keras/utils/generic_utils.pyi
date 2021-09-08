from tensorflow.python.util import nest as nest, tf_contextlib as tf_contextlib, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class CustomObjectScope:
    custom_objects: Any = ...
    backup: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...

def custom_object_scope(*args: Any): ...
def get_custom_objects(): ...
def serialize_keras_class_and_config(cls_name: Any, cls_config: Any): ...
def register_keras_serializable(package: str = ..., name: Optional[Any] = ...): ...
def get_registered_name(obj: Any): ...
def skip_failed_serialization() -> None: ...
def get_registered_object(name: Any, custom_objects: Optional[Any] = ..., module_objects: Optional[Any] = ...): ...
def serialize_keras_object(instance: Any): ...
def get_custom_objects_by_name(item: Any, custom_objects: Optional[Any] = ...): ...
def class_and_config_for_serialized_keras_object(config: Any, module_objects: Optional[Any] = ..., custom_objects: Optional[Any] = ..., printable_module_name: str = ...): ...
def deserialize_keras_object(identifier: Any, module_objects: Optional[Any] = ..., custom_objects: Optional[Any] = ..., printable_module_name: str = ...): ...
def func_dump(func: Any): ...
def func_load(code: Any, defaults: Optional[Any] = ..., closure: Optional[Any] = ..., globs: Optional[Any] = ...): ...
def has_arg(fn: Any, name: Any, accept_all: bool = ...): ...

class Progbar:
    target: Any = ...
    width: Any = ...
    verbose: Any = ...
    interval: Any = ...
    unit_name: Any = ...
    stateful_metrics: Any = ...
    def __init__(self, target: Any, width: int = ..., verbose: int = ..., interval: float = ..., stateful_metrics: Optional[Any] = ..., unit_name: str = ...) -> None: ...
    def update(self, current: Any, values: Optional[Any] = ..., finalize: Optional[Any] = ...) -> None: ...
    def add(self, n: Any, values: Optional[Any] = ...) -> None: ...

def make_batches(size: Any, batch_size: Any): ...
def slice_arrays(arrays: Any, start: Optional[Any] = ..., stop: Optional[Any] = ...): ...
def to_list(x: Any): ...
def to_snake_case(name: Any): ...
def is_all_none(structure: Any): ...
def check_for_unexpected_keys(name: Any, input_dict: Any, expected_values: Any) -> None: ...
def validate_kwargs(kwargs: Any, allowed_kwargs: Any, error_message: str = ...) -> None: ...
def validate_config(config: Any): ...
def default(method: Any): ...
def is_default(method: Any): ...