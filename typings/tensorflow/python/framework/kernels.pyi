from tensorflow.core.framework import kernel_def_pb2 as kernel_def_pb2
from tensorflow.python.util import compat as compat
from typing import Any

def get_all_registered_kernels(): ...
def get_registered_kernels_for_op(name: Any): ...
