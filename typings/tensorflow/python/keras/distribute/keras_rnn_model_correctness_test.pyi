from tensorflow.python import keras as keras, tf2 as tf2
from tensorflow.python.distribute import combinations as combinations, tpu_strategy as tpu_strategy
from tensorflow.python.eager import context as context
from tensorflow.python.keras import testing_utils as testing_utils
from tensorflow.python.keras.distribute import keras_correctness_test_base as keras_correctness_test_base
from tensorflow.python.keras.mixed_precision.experimental import policy as policy
from tensorflow.python.platform import test as test
from typing import Any, Optional

class _DistributionStrategyRnnModelCorrectnessTest(keras_correctness_test_base.TestDistributionStrategyEmbeddingModelCorrectnessBase):
    def get_model(self, max_words: int = ..., initial_weights: Optional[Any] = ..., distribution: Optional[Any] = ..., input_shapes: Optional[Any] = ...): ...

class DistributionStrategyGruModelCorrectnessTest(_DistributionStrategyRnnModelCorrectnessTest):
    def test_gru_model_correctness(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...

class DistributionStrategyLstmModelCorrectnessTest(_DistributionStrategyRnnModelCorrectnessTest):
    def test_lstm_model_correctness(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
    def test_lstm_model_correctness_mixed_precision(self, distribution: Any, use_numpy: Any, use_validation_data: Any) -> None: ...
