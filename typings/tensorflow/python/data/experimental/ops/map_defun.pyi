from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from typing import Any

def map_defun(fn: Any, elems: Any, output_dtypes: Any, output_shapes: Any, max_intra_op_parallelism: int = ...): ...
