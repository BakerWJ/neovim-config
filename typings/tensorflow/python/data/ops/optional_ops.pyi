import abc
from tensorflow.python.data.util import structure as structure
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional as _Optional

class Optional(composite_tensor.CompositeTensor, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def has_value(self, name: _Optional[Any] = ...) -> Any: ...
    @abc.abstractmethod
    def get_value(self, name: _Optional[Any] = ...) -> Any: ...
    @property
    @abc.abstractmethod
    def value_structure(self) -> Any: ...
    @staticmethod
    def from_value(value: Any): ...
    @staticmethod
    def none_from_structure(value_structure: Any): ...

class _OptionalImpl(Optional):
    def __init__(self, variant_tensor: Any, value_structure: Any) -> None: ...
    def has_value(self, name: _Optional[Any] = ...): ...
    def get_value(self, name: _Optional[Any] = ...): ...
    @property
    def value_structure(self): ...

class OptionalSpec(type_spec.TypeSpec):
    def __init__(self, value_structure: Any) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value: Any): ...
