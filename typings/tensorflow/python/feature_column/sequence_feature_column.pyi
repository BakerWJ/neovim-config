from tensorflow.python.feature_column import feature_column_v2 as fc
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, parsing_ops as parsing_ops, sparse_ops as sparse_ops
from tensorflow.python.util.tf_export import keras_export as keras_export, tf_export as tf_export
from typing import Any, Optional

class SequenceFeatures(fc._BaseFeaturesLayer):
    def __init__(self, feature_columns: Any, trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, features: Any): ...

def concatenate_context_input(context_input: Any, sequence_input: Any): ...
def sequence_categorical_column_with_identity(key: Any, num_buckets: Any, default_value: Optional[Any] = ...): ...
def sequence_categorical_column_with_hash_bucket(key: Any, hash_bucket_size: Any, dtype: Any = ...): ...
def sequence_categorical_column_with_vocabulary_file(key: Any, vocabulary_file: Any, vocabulary_size: Optional[Any] = ..., num_oov_buckets: int = ..., default_value: Optional[Any] = ..., dtype: Any = ...): ...
def sequence_categorical_column_with_vocabulary_list(key: Any, vocabulary_list: Any, dtype: Optional[Any] = ..., default_value: int = ..., num_oov_buckets: int = ...): ...
def sequence_numeric_column(key: Any, shape: Any = ..., default_value: float = ..., dtype: Any = ..., normalizer_fn: Optional[Any] = ...): ...

class SequenceNumericColumn(fc.SequenceDenseColumn):
    @property
    def name(self): ...
    @property
    def parse_example_spec(self): ...
    def transform_feature(self, transformation_cache: Any, state_manager: Any): ...
    @property
    def variable_shape(self): ...
    def get_sequence_dense_tensor(self, transformation_cache: Any, state_manager: Any): ...
    @property
    def parents(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ..., columns_by_name: Optional[Any] = ...): ...
