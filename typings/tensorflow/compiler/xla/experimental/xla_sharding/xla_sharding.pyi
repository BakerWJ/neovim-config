from tensorflow.compiler.xla import xla_data_pb2 as xla_data_pb2
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from typing import Any, Optional

class Sharding:
    def __init__(self, proto: Optional[Any] = ...) -> None: ...
    @classmethod
    def replicate(cls): ...
    @classmethod
    def assign_device(cls, core: Any): ...
    @classmethod
    def tile(cls, tile_assignment: Any): ...
    @classmethod
    def split(cls, tensor: Any, split_dimension: Any, num_devices: Any, input_shape: Optional[Any] = ...): ...
    def apply_to_tensor(self, tensor: Any, assign_tuple_sharding: bool = ...) -> None: ...
    @property
    def proto(self): ...

def replicate(tensor: Any, assign_tuple_sharding: bool = ..., use_sharding_op: bool = ...): ...
def assign_device(tensor: Any, device: Any, assign_tuple_sharding: bool = ..., use_sharding_op: bool = ...): ...
def tile(tensor: Any, tile_assignment: Any, assign_tuple_sharding: bool = ..., use_sharding_op: bool = ...): ...
def split(tensor: Any, split_dimension: Any, num_devices: Any, assign_tuple_sharding: bool = ..., use_sharding_op: bool = ..., input_shape: Optional[Any] = ...): ...
