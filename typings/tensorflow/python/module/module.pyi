from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import variables as variables
from tensorflow.python.training.tracking import tracking as tracking
from tensorflow.python.util import nest as nest, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class Module(tracking.AutoTrackable):
    def __init__(self, name: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def name_scope(self): ...
    @property
    def variables(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def submodules(self): ...
    @classmethod
    def with_name_scope(cls, method: Any): ...

def valid_identifier(name: Any): ...
def camel_to_snake(value: Any): ...
