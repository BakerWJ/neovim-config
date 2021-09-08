from tensorflow.python.framework import tensor_shape as tensor_shape
from typing import Any, Optional

class ShardingPolicy:
    def __init__(self) -> None: ...
    def freeze(self) -> None: ...
    @property
    def number_of_shards(self): ...
    def set_number_of_shards(self, number_of_shards: Any) -> None: ...
    @property
    def shard_dimension(self): ...
    def set_shard_dimension(self, shard_dimension: Any) -> None: ...
    def merge(self, other: Any) -> None: ...
    def get_sharded_shape(self, shape: Any, shard_index: Optional[Any] = ...): ...
    def get_unsharded_shape(self, shapes: Any): ...