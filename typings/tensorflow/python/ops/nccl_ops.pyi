from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import device as device, ops as ops
from tensorflow.python.ops import gen_nccl_ops as gen_nccl_ops
from typing import Any

def all_sum(tensors: Any): ...
def all_prod(tensors: Any): ...
def all_min(tensors: Any): ...
def all_max(tensors: Any): ...
def reduce_sum(tensors: Any): ...
def broadcast(tensor: Any): ...
