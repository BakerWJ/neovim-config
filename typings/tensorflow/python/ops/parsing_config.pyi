from collections import namedtuple
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, sparse_ops as sparse_ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

ragged_tensor: Any
ragged_math_ops: Any

class VarLenFeature: ...

class RaggedFeature:

    RowSplits = namedtuple('RowSplits', ['key'])

    RowLengths = namedtuple('RowLengths', ['key'])

    RowStarts = namedtuple('RowStarts', ['key'])

    RowLimits = namedtuple('RowLimits', ['key'])

    ValueRowIds = namedtuple('ValueRowIds', ['key'])

    UniformRowLength = namedtuple('UniformRowLength', ['length'])
    def __new__(cls, dtype: Any, value_key: Optional[Any] = ..., partitions: Any = ..., row_splits_dtype: Any = ..., validate: bool = ...): ...

class SparseFeature:
    def __new__(cls, index_key: Any, value_key: Any, dtype: Any, size: Any, already_sorted: bool = ...): ...

class FixedLenFeature:
    def __new__(cls, shape: Any, dtype: Any, default_value: Optional[Any] = ...): ...

class FixedLenSequenceFeature:
    def __new__(cls, shape: Any, dtype: Any, allow_missing: bool = ..., default_value: Optional[Any] = ...): ...

class _ParseOpParams:
    sparse_keys: Any = ...
    sparse_types: Any = ...
    dense_keys: Any = ...
    dense_types: Any = ...
    dense_shapes: Any = ...
    dense_defaults: Any = ...
    ragged_keys: Any = ...
    ragged_value_types: Any = ...
    ragged_split_types: Any = ...
    def __init__(self, sparse_keys: Optional[Any] = ..., sparse_types: Optional[Any] = ..., dense_keys: Optional[Any] = ..., dense_types: Optional[Any] = ..., dense_defaults: Optional[Any] = ..., dense_shapes: Optional[Any] = ..., ragged_keys: Optional[Any] = ..., ragged_value_types: Optional[Any] = ..., ragged_split_types: Optional[Any] = ...) -> None: ...
    @classmethod
    def from_features(cls, features: Any, types: Any): ...
    @property
    def dense_shapes_as_proto(self): ...
    @property
    def num_features(self): ...
    @property
    def dense_defaults_vec(self): ...
