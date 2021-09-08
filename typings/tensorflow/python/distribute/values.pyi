from collections import namedtuple
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, reduce_util as reduce_util
from tensorflow.python.eager import context as context, tape as tape
from tensorflow.python.framework import composite_tensor as composite_tensor, ops as ops, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, variables as variables_lib
from tensorflow.python.training.saving import saveable_object as saveable_object, saveable_object_util as saveable_object_util
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class DistributedValues:
    def __init__(self, values: Any) -> None: ...

class DistributedDelegate(DistributedValues):
    def __getattr__(self, name: Any): ...
    @property
    def values(self): ...
    def __add__(self, o: Any): ...
    def __radd__(self, o: Any): ...
    def __sub__(self, o: Any): ...
    def __rsub__(self, o: Any): ...
    def __mul__(self, o: Any): ...
    def __rmul__(self, o: Any): ...
    def __truediv__(self, o: Any): ...
    def __rtruediv__(self, o: Any): ...
    def __floordiv__(self, o: Any): ...
    def __rfloordiv__(self, o: Any): ...
    def __mod__(self, o: Any): ...
    def __rmod__(self, o: Any): ...
    def __lt__(self, o: Any) -> Any: ...
    def __le__(self, o: Any) -> Any: ...
    def __gt__(self, o: Any) -> Any: ...
    def __ge__(self, o: Any) -> Any: ...
    def __and__(self, o: Any): ...
    def __rand__(self, o: Any): ...
    def __or__(self, o: Any): ...
    def __ror__(self, o: Any): ...
    def __xor__(self, o: Any): ...
    def __rxor__(self, o: Any): ...
    def __getitem__(self, o: Any): ...
    def __pow__(self, o: Any, modulo: Optional[Any] = ...): ...
    def __rpow__(self, o: Any): ...
    def __invert__(self): ...
    def __neg__(self): ...
    def __abs__(self): ...
    def __div__(self, o: Any): ...
    def __rdiv__(self, o: Any): ...
    def __matmul__(self, o: Any): ...
    def __rmatmul__(self, o: Any): ...

class PerReplica(DistributedValues, composite_tensor.CompositeTensor):
    @property
    def values(self): ...

class PerReplicaSpec(type_spec.TypeSpec):
    value_type: Any = ...
    def __init__(self, *value_specs: Any) -> None: ...

class Mirrored(DistributedDelegate): ...

DistributedVarOp = namedtuple('DistributedVarOp', ['name', 'graph', 'traceback', 'type'])

class DistributedVariable(DistributedDelegate, variables_lib.Variable):
    def __init__(self, strategy: Any, values: Any) -> None: ...
    def is_initialized(self, name: Optional[Any] = ...): ...
    @property
    def initializer(self): ...
    def initialized_value(self): ...
    @property
    def initial_value(self): ...
    @property
    def constraint(self): ...
    @property
    def graph(self): ...
    @property
    def name(self): ...
    @property
    def dtype(self): ...
    @property
    def shape(self): ...
    @property
    def synchronization(self): ...
    @property
    def handle(self): ...
    def eval(self, session: Optional[Any] = ...): ...
    @property
    def device(self): ...
    @property
    def trainable(self): ...
    @property
    def distribute_strategy(self): ...
    def get_shape(self): ...
    def to_proto(self, export_scope: Optional[Any] = ...): ...
    @property
    def op(self): ...
    def read_value(self): ...
    def value(self): ...

def validate_colocate_distributed_variable(v: Any, extended: Any) -> None: ...
def validate_colocate(v: Any, extended: Any) -> None: ...

class _MirroredSaveable(saveable_object_util.ResourceVariableSaveable):
    def __init__(self, mirrored_variable: Any, primary_variable: Any, name: Any) -> None: ...
    def restore(self, restored_tensors: Any, restored_shapes: Any): ...

def create_mirrored_variable(strategy: Any, real_mirrored_creator: Any, mirrored_cls: Any, sync_on_read_cls: Any, **kwargs: Any): ...

class MirroredVariable(DistributedVariable, Mirrored):
    def __init__(self, strategy: Any, values: Any, aggregation: Any) -> None: ...
    def assign_sub(self, *args: Any, **kwargs: Any): ...
    def assign_add(self, *args: Any, **kwargs: Any): ...
    def assign(self, *args: Any, **kwargs: Any): ...
    def scatter_sub(self, *args: Any, **kwargs: Any): ...
    def scatter_add(self, *args: Any, **kwargs: Any): ...
    def scatter_mul(self, *args: Any, **kwargs: Any): ...
    def scatter_div(self, *args: Any, **kwargs: Any): ...
    def scatter_min(self, *args: Any, **kwargs: Any): ...
    def scatter_max(self, *args: Any, **kwargs: Any): ...
    def scatter_update(self, *args: Any, **kwargs: Any): ...
    @property
    def aggregation(self): ...

def is_distributed_variable(v: Any): ...

class _SyncOnReadSaveable(saveable_object.SaveableObject):
    def __init__(self, sync_on_read_variable: Any, name: Any): ...
    def restore(self, restored_tensors: Any, restored_shapes: Any): ...

class SyncOnReadVariable(DistributedVariable):
    def __init__(self, strategy: Any, values: Any, aggregation: Any) -> None: ...
    def assign_sub(self, *args: Any, **kwargs: Any): ...
    def assign_add(self, *args: Any, **kwargs: Any): ...
    def assign(self, *args: Any, **kwargs: Any): ...
    def value(self): ...
    def numpy(self): ...
    @property
    def aggregation(self): ...

def regroup(values: Any, wrap_class: Any = ..., always_wrap: bool = ...): ...
def select_replica(replica_id: Any, structured: Any): ...
def select_replica_mirrored(replica_id: Any, structured: Any): ...
def update_regroup(extended: Any, updates: Any, group: Any): ...
def value_container(val: Any): ...

class AggregatingVariable(variables_lib.Variable):
    def __init__(self, strategy: Any, v: Any, aggregation: Any) -> None: ...
    def get(self): ...
    @property
    def distribute_strategy(self): ...
    def __getattr__(self, name: Any): ...
    def assign_sub(self, *args: Any, **kwargs: Any): ...
    def assign_add(self, *args: Any, **kwargs: Any): ...
    def assign(self, *args: Any, **kwargs: Any): ...
    @property
    def initializer(self): ...
    def initialized_value(self): ...
    @property
    def initial_value(self): ...
    @property
    def op(self): ...
    def read_value(self): ...
    def eval(self, session: Optional[Any] = ...): ...
    @property
    def graph(self): ...
    @property
    def device(self): ...
    @property
    def shape(self): ...
    @property
    def aggregation(self): ...
    @property
    def synchronization(self): ...
    @property
    def name(self): ...
    @property
    def trainable(self): ...
    @property
    def dtype(self): ...
    def __add__(self, o: Any): ...
    def __radd__(self, o: Any): ...
    def __sub__(self, o: Any): ...
    def __rsub__(self, o: Any): ...
    def __mul__(self, o: Any): ...
    def __rmul__(self, o: Any): ...
    def __truediv__(self, o: Any): ...
    def __rtruediv__(self, o: Any): ...
    def __floordiv__(self, o: Any): ...
    def __rfloordiv__(self, o: Any): ...
    def __mod__(self, o: Any): ...
    def __rmod__(self, o: Any): ...
    def __lt__(self, o: Any) -> Any: ...
    def __le__(self, o: Any) -> Any: ...
    def __gt__(self, o: Any) -> Any: ...
    def __ge__(self, o: Any) -> Any: ...
    def __and__(self, o: Any): ...
    def __rand__(self, o: Any): ...
    def __or__(self, o: Any): ...
    def __ror__(self, o: Any): ...
    def __xor__(self, o: Any): ...
    def __rxor__(self, o: Any): ...
    def __getitem__(self, o: Any): ...
    def __pow__(self, o: Any, modulo: Optional[Any] = ...): ...
    def __rpow__(self, o: Any): ...
    def __invert__(self): ...
    def __neg__(self): ...
    def __abs__(self): ...
    def __div__(self, o: Any): ...
    def __rdiv__(self, o: Any): ...
    def __matmul__(self, o: Any): ...
    def __rmatmul__(self, o: Any): ...