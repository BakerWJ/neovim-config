import abc
from typing import Any, Optional

class _Mapping:
    def __new__(cls, x: Optional[Any] = ..., y: Optional[Any] = ..., ildj_map: Optional[Any] = ..., kwargs: Optional[Any] = ...): ...
    @property
    def x_key(self): ...
    @property
    def y_key(self): ...
    def merge(self, x: Optional[Any] = ..., y: Optional[Any] = ..., ildj_map: Optional[Any] = ..., kwargs: Optional[Any] = ..., mapping: Optional[Any] = ...): ...

class Bijector(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, graph_parents: Optional[Any] = ..., is_constant_jacobian: bool = ..., validate_args: bool = ..., dtype: Optional[Any] = ..., forward_min_event_ndims: Optional[Any] = ..., inverse_min_event_ndims: Optional[Any] = ..., name: Optional[Any] = ...) -> Any: ...
    @property
    def graph_parents(self): ...
    @property
    def forward_min_event_ndims(self): ...
    @property
    def inverse_min_event_ndims(self): ...
    @property
    def is_constant_jacobian(self): ...
    @property
    def validate_args(self): ...
    @property
    def dtype(self): ...
    @property
    def name(self): ...
    def forward_event_shape_tensor(self, input_shape: Any, name: str = ...): ...
    def forward_event_shape(self, input_shape: Any): ...
    def inverse_event_shape_tensor(self, output_shape: Any, name: str = ...): ...
    def inverse_event_shape(self, output_shape: Any): ...
    def forward(self, x: Any, name: str = ...): ...
    def inverse(self, y: Any, name: str = ...): ...
    def inverse_log_det_jacobian(self, y: Any, event_ndims: Any, name: str = ...): ...
    def forward_log_det_jacobian(self, x: Any, event_ndims: Any, name: str = ...): ...
