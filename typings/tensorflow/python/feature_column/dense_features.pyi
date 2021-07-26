from tensorflow.python.feature_column import feature_column_v2 as fc
from tensorflow.python.framework import ops as ops
from tensorflow.python.util import serialization as serialization
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class DenseFeatures(fc._BaseFeaturesLayer):
    def __init__(self, feature_columns: Any, trainable: bool = ..., name: Optional[Any] = ..., partitioner: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def call(self, features: Any, cols_to_output_tensors: Optional[Any] = ...): ...
