from tensorflow.python.framework import ops as ops
from tensorflow.python.util import lazy_loader as lazy_loader
from typing import Any

training: Any
training_v1: Any
base_layer: Any
base_layer_v1: Any

class ModelVersionSelector:
    def __new__(cls, *args: Any, **kwargs: Any): ...

class LayerVersionSelector:
    def __new__(cls, *args: Any, **kwargs: Any): ...

def swap_class(cls, v2_cls: Any, v1_cls: Any, eager_enabled: Any): ...
def disallow_legacy_graph(cls_name: Any, method_name: Any) -> None: ...
