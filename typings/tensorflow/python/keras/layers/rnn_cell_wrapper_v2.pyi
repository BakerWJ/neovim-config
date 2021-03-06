from tensorflow.python.keras.layers import recurrent as recurrent
from tensorflow.python.ops import rnn_cell_wrapper_impl as rnn_cell_wrapper_impl
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _RNNCellWrapperV2(recurrent.AbstractRNNCell):
    cell: Any = ...
    def __init__(self, cell: Any, *args: Any, **kwargs: Any) -> None: ...
    def call(self, inputs: Any, state: Any, **kwargs: Any): ...
    built: bool = ...
    def build(self, inputs_shape: Any) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any, custom_objects: Optional[Any] = ...): ...

class DropoutWrapper(rnn_cell_wrapper_impl.DropoutWrapperBase, _RNNCellWrapperV2):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ResidualWrapper(rnn_cell_wrapper_impl.ResidualWrapperBase, _RNNCellWrapperV2):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class DeviceWrapper(rnn_cell_wrapper_impl.DeviceWrapperBase, _RNNCellWrapperV2):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
