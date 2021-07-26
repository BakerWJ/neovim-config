from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, func_graph as func_graph, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_resource_variable_ops as gen_resource_variable_ops
from tensorflow.python.util import nest as nest
from typing import Any

def rewrite_grad_indexed_slices(grads: Any, body_grad_graph: Any, loop_vars: Any, forward_inputs: Any): ...
