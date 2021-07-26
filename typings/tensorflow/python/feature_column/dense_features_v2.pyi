from tensorflow.python.feature_column import dense_features as dense_features
from tensorflow.python.framework import ops as ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class DenseFeatures(dense_features.DenseFeatures):
    def __init__(self, feature_columns: Any, trainable: bool = ..., name: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def build(self, _: Any) -> None: ...
