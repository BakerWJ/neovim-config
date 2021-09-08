from tensorflow.python import keras as keras
from tensorflow.python.distribute import combinations as combinations, strategy_combinations as strategy_combinations
from tensorflow.python.keras.distribute import keras_correctness_test_base as keras_correctness_test_base
from tensorflow.python.platform import test as test
from typing import Any, Optional

def strategies_for_stateful_embedding_model(): ...
def test_combinations_for_stateful_embedding_model(): ...

class DistributionStrategyStatefulLstmModelCorrectnessTest(keras_correctness_test_base.TestDistributionStrategyEmbeddingModelCorrectnessBase):
    def get_model(self, max_words: int = ..., initial_weights: Optional[Any] = ..., distribution: Optional[Any] = ..., input_shapes: Optional[Any] = ...): ...
    def disabled_test_stateful_lstm_model_correctness(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
    def test_incorrectly_use_multiple_cores_for_stateful_lstm_model(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...