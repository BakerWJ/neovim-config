from absl.testing import parameterized
from tensorflow.python import keras as keras, tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import testing_utils as testing_utils
from tensorflow.python.platform import test as test
from tensorflow.python.util import nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from typing import Any, Optional

class TestCase(test.TestCase, parameterized.TestCase):
    def tearDown(self) -> None: ...

def run_with_all_saved_model_formats(test_or_class: Optional[Any] = ..., exclude_formats: Optional[Any] = ...): ...
def run_with_all_model_types(test_or_class: Optional[Any] = ..., exclude_models: Optional[Any] = ...): ...
def run_all_keras_modes(test_or_class: Optional[Any] = ..., config: Optional[Any] = ..., always_skip_v1: bool = ..., always_skip_eager: bool = ...): ...
