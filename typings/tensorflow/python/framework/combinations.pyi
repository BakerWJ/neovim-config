from tensorflow.python import tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, test_combinations as test_combinations
from typing import Any

class EagerGraphCombination(test_combinations.TestCombination):
    def context_managers(self, kwargs: Any): ...
    def parameter_modifiers(self): ...

class TFVersionCombination(test_combinations.TestCombination):
    def should_execute_combination(self, kwargs: Any): ...
    def parameter_modifiers(self): ...

generate: Any
combine: Any
times: Any
NamedObject: Any
