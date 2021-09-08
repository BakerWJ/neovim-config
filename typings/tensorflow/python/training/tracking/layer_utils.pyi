from tensorflow.python.util import object_identity as object_identity
from typing import Any

def is_layer(obj: Any): ...
def has_weights(obj: Any): ...
def cache_recursive_attribute(key: Any): ...
def invalidate_recursive_cache(key: Any): ...

class MutationSentinel:
    def mark_as(self, value: bool) -> bool: ...
    @property
    def in_cached_state(self): ...

class AttributeSentinel:
    attributes: Any = ...
    always_propagate: Any = ...
    def __init__(self, always_propagate: bool = ...) -> None: ...
    def add_parent(self, node: AttributeSentinel) -> None: ...
    def get(self, key: str) -> bool: ...
    def mark_cached(self, key: str) -> None: ...
    def invalidate(self, key: str) -> None: ...
    def invalidate_all(self) -> None: ...

def filter_empty_layer_containers(layer_list: Any) -> None: ...
def gather_trainable_weights(trainable: Any, sub_layers: Any, extra_variables: Any): ...
def gather_non_trainable_weights(trainable: Any, sub_layers: Any, extra_variables: Any): ...