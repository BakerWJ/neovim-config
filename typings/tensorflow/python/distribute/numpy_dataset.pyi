from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, variable_scope as variable_scope
from tensorflow.python.util import nest as nest
from typing import Any

def init_var_from_numpy(input_var: Any, numpy_input: Any, session: Any) -> None: ...
def one_host_numpy_dataset(numpy_input: Any, colocate_with: Any, session: Any): ...

class SingleDevice:
    device: Any = ...
    def __init__(self, device: Any) -> None: ...
