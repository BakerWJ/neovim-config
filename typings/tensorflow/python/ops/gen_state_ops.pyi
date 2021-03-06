from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def assign(ref: Any, value: Any, validate_shape: bool = ..., use_locking: bool = ..., name: Optional[Any] = ...): ...

Assign: Any

def assign_eager_fallback(ref: Any, value: Any, validate_shape: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def assign_add(ref: Any, value: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

AssignAdd: Any

def assign_add_eager_fallback(ref: Any, value: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def assign_sub(ref: Any, value: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

AssignSub: Any

def assign_sub_eager_fallback(ref: Any, value: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def count_up_to(ref: Any, limit: Any, name: Optional[Any] = ...): ...

CountUpTo: Any

def count_up_to_eager_fallback(ref: Any, limit: Any, name: Any, ctx: Any) -> None: ...
def destroy_temporary_variable(ref: Any, var_name: Any, name: Optional[Any] = ...): ...

DestroyTemporaryVariable: Any

def destroy_temporary_variable_eager_fallback(ref: Any, var_name: Any, name: Any, ctx: Any) -> None: ...
def is_variable_initialized(ref: Any, name: Optional[Any] = ...): ...

IsVariableInitialized: Any

def is_variable_initialized_eager_fallback(ref: Any, name: Any, ctx: Any) -> None: ...
def resource_count_up_to(resource: Any, limit: Any, T: Any, name: Optional[Any] = ...): ...

ResourceCountUpTo: Any

def resource_count_up_to_eager_fallback(resource: Any, limit: Any, T: Any, name: Any, ctx: Any): ...
def resource_scatter_nd_add(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ResourceScatterNdAdd: Any

def resource_scatter_nd_add_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any): ...
def resource_scatter_nd_sub(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ResourceScatterNdSub: Any

def resource_scatter_nd_sub_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any): ...
def resource_scatter_nd_update(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ResourceScatterNdUpdate: Any

def resource_scatter_nd_update_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any): ...
def scatter_add(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterAdd: Any

def scatter_add_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_div(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterDiv: Any

def scatter_div_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_max(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterMax: Any

def scatter_max_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_min(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterMin: Any

def scatter_min_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_mul(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterMul: Any

def scatter_mul_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_nd_add(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterNdAdd: Any

def scatter_nd_add_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_nd_sub(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterNdSub: Any

def scatter_nd_sub_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_nd_update(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterNdUpdate: Any

def scatter_nd_update_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_sub(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterSub: Any

def scatter_sub_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def scatter_update(ref: Any, indices: Any, updates: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...

ScatterUpdate: Any

def scatter_update_eager_fallback(ref: Any, indices: Any, updates: Any, use_locking: Any, name: Any, ctx: Any) -> None: ...
def temporary_variable(shape: Any, dtype: Any, var_name: str = ..., name: Optional[Any] = ...): ...

TemporaryVariable: Any

def temporary_variable_eager_fallback(shape: Any, dtype: Any, var_name: Any, name: Any, ctx: Any) -> None: ...
def variable(shape: Any, dtype: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

Variable: Any

def variable_eager_fallback(shape: Any, dtype: Any, container: Any, shared_name: Any, name: Any, ctx: Any) -> None: ...
def variable_v2(shape: Any, dtype: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

VariableV2: Any

def variable_v2_eager_fallback(shape: Any, dtype: Any, container: Any, shared_name: Any, name: Any, ctx: Any) -> None: ...
