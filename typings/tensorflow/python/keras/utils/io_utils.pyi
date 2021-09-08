from tensorflow.python.framework import tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

class HDF5Matrix:
    refs: Any = ...
    data: Any = ...
    start: Any = ...
    end: Any = ...
    normalizer: Any = ...
    def __init__(self, datapath: Any, dataset: Any, start: int = ..., end: Optional[Any] = ..., normalizer: Optional[Any] = ...) -> None: ...
    def __len__(self): ...
    def __getitem__(self, key: Any): ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    @property
    def ndim(self): ...
    @property
    def size(self): ...

def ask_to_proceed_with_overwrite(filepath: Any): ...