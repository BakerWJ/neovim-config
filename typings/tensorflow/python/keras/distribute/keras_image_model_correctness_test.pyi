from tensorflow.python import keras as keras
from tensorflow.python.distribute import combinations as combinations
from tensorflow.python.eager import context as context
from tensorflow.python.keras.distribute import keras_correctness_test_base as keras_correctness_test_base
from tensorflow.python.keras.optimizer_v2 import gradient_descent as gradient_descent
from tensorflow.python.platform import test as test
from typing import Any, Optional

class DistributionStrategyCnnCorrectnessTest(keras_correctness_test_base.TestDistributionStrategyCorrectnessBase):
    def get_model(self, initial_weights: Optional[Any] = ..., distribution: Optional[Any] = ..., input_shapes: Optional[Any] = ...): ...
    def get_data(self): ...
    def get_data_with_partial_last_batch_eval(self): ...
    def test_cnn_correctness(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
    def test_cnn_with_batch_norm_correctness(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
    def test_cnn_with_sync_batch_norm_correctness(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
    def test_cnn_correctness_with_partial_last_batch_eval(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
    def test_cnn_with_batch_norm_correctness_and_partial_last_batch_eval(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
