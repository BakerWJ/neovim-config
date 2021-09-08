from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from typing import Any

def get_gradients_through_compute_gradients(optimizer: Any, loss: Any, activations: Any): ...
def create_dummy_table_variables(tpu_embedding: Any): ...
def hook_dummy_table_variables_to_activations(tpu_embedding: Any, activations: Any, dummy_table_variables: Any): ...
def get_gradients_through_dummy_table_variables(tpu_embedding: Any): ...