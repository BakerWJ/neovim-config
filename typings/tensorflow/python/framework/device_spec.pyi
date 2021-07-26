from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class DeviceSpecV2:
    def __init__(self, job: Optional[Any] = ..., replica: Optional[Any] = ..., task: Optional[Any] = ..., device_type: Optional[Any] = ..., device_index: Optional[Any] = ...) -> None: ...
    def to_string(self): ...
    @classmethod
    def from_string(cls, spec: Any): ...
    def parse_from_string(self, spec: Any): ...
    def make_merged_spec(self, dev: Any): ...
    def replace(self, **kwargs: Any): ...
    @property
    def job(self): ...
    @property
    def replica(self): ...
    @property
    def task(self): ...
    @property
    def device_type(self): ...
    @property
    def device_index(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class DeviceSpecV1(DeviceSpecV2):
    __doc__: Any = ...
    def job(self, job: Any) -> None: ...
    def replica(self, replica: Any) -> None: ...
    def task(self, task: Any) -> None: ...
    def device_type(self, device_type: Any) -> None: ...
    def device_index(self, device_index: Any) -> None: ...
    def __hash__(self) -> Any: ...
    def to_string(self): ...
    def parse_from_string(self, spec: Any): ...
    def merge_from(self, dev: Any) -> None: ...
