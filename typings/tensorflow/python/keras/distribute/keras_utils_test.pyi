from absl.testing import parameterized
from tensorflow.python import keras as keras
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import combinations as combinations, parameter_server_strategy as parameter_server_strategy, strategy_combinations as strategy_combinations, tpu_strategy as tpu_strategy, values as values
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes
from tensorflow.python.keras import losses as losses
from tensorflow.python.keras.distribute import distributed_training_utils as distributed_training_utils
from tensorflow.python.platform import test as test
from tensorflow.python.training import gradient_descent as gradient_descent
from typing import Any

class Counter(keras.callbacks.Callback):
    method_counts: Any = ...
    def __init__(self) -> None: ...
    def wrap_with_counts(self, method_name: Any, method: Any): ...

class TestDistributionStrategyWithCallbacks(test.TestCase, parameterized.TestCase):
    def test_callbacks_in_fit(self, distribution: Any) -> None: ...
    def test_callbacks_in_eval(self, distribution: Any) -> None: ...
    def test_callbacks_in_predict(self, distribution: Any) -> None: ...

class TestDistributionStrategyErrorCases(test.TestCase, parameterized.TestCase):
    def test_validating_dataset_input_tensors_with_shape_mismatch(self, distribution: Any) -> None: ...
    def test_validating_dataset_input_tensors_with_dtype_mismatch(self, distribution: Any) -> None: ...
    def test_unsupported_features(self, distribution: Any, mode: Any) -> None: ...
    dense: Any = ...
    def test_distribution_strategy_on_subclassed_model(self, distribution: Any): ...
    def test_distribution_strategy_on_deferred_sequential_model(self, distribution: Any) -> None: ...
    def test_standalone_loss_without_loss_reduction(self, distribution: Any) -> None: ...

class TestDistributionStrategyWithLossMasking(test.TestCase, parameterized.TestCase):
    def test_masking(self, distribution: Any, optimizer: Any) -> None: ...

class TestDistributionStrategyWithNormalizationLayer(test.TestCase, parameterized.TestCase):
    def test_batchnorm_correctness(self, distribution: Any, fused: Any, optimizer: Any) -> None: ...

class TestDistributionStrategySaveLoadWeights(test.TestCase, parameterized.TestCase):
    def test_save_load_h5(self, distribution: Any, optimizer: Any) -> None: ...
    def test_save_load_trackable(self, distribution: Any, optimizer: Any) -> None: ...

class TestDistributionStrategyValidation(test.TestCase, parameterized.TestCase):
    def test_layer_outside_scope(self, distribution: Any) -> None: ...
    def test_model_outside_scope(self, distribution: Any) -> None: ...

class TestDistributionStrategyWithStaticShapes(test.TestCase, parameterized.TestCase):
    def test_input_batch_size_not_divisible_by_num_replicas(self, distribution: Any) -> None: ...
    def test_static_input_batch_size(self, distribution: Any) -> None: ...
