from tensorflow.core.protobuf import saver_pb2 as saver_pb2
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, gen_io_ops as gen_io_ops, io_ops as io_ops, string_ops as string_ops
from tensorflow.python.training.saving import saveable_hook as saveable_hook, saveable_object as saveable_object, saveable_object_util as saveable_object_util
from tensorflow.python.util import nest as nest
from typing import Any

class _SingleDeviceSaver:
    def __init__(self, saveable_objects: Any) -> None: ...
    def save(self, file_prefix: Any): ...
    def restore(self, file_prefix: Any): ...

def sharded_filename(filename_tensor: Any, shard: Any, num_shards: Any): ...

class MultiDeviceSaver:
    def __init__(self, saveable_objects: Any) -> None: ...
    def to_proto(self): ...
    def save(self, file_prefix: Any): ...
    def restore(self, file_prefix: Any): ...