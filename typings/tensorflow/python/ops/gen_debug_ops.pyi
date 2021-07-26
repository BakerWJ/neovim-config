from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def copy(input: Any, tensor_name: str = ..., debug_ops_spec: Any = ..., name: Optional[Any] = ...): ...

Copy: Any

def copy_eager_fallback(input: Any, tensor_name: Any, debug_ops_spec: Any, name: Any, ctx: Any): ...
def copy_host(input: Any, tensor_name: str = ..., debug_ops_spec: Any = ..., name: Optional[Any] = ...): ...

CopyHost: Any

def copy_host_eager_fallback(input: Any, tensor_name: Any, debug_ops_spec: Any, name: Any, ctx: Any): ...
def debug_identity(input: Any, device_name: str = ..., tensor_name: str = ..., debug_urls: Any = ..., gated_grpc: bool = ..., name: Optional[Any] = ...): ...

DebugIdentity: Any

def debug_identity_eager_fallback(input: Any, device_name: Any, tensor_name: Any, debug_urls: Any, gated_grpc: Any, name: Any, ctx: Any): ...
def debug_identity_v2(input: Any, tfdbg_context_id: str = ..., op_name: str = ..., output_slot: int = ..., tensor_debug_mode: int = ..., debug_urls: Any = ..., name: Optional[Any] = ...): ...

DebugIdentityV2: Any

def debug_identity_v2_eager_fallback(input: Any, tfdbg_context_id: Any, op_name: Any, output_slot: Any, tensor_debug_mode: Any, debug_urls: Any, name: Any, ctx: Any): ...
def debug_nan_count(input: Any, device_name: str = ..., tensor_name: str = ..., debug_urls: Any = ..., gated_grpc: bool = ..., name: Optional[Any] = ...): ...

DebugNanCount: Any

def debug_nan_count_eager_fallback(input: Any, device_name: Any, tensor_name: Any, debug_urls: Any, gated_grpc: Any, name: Any, ctx: Any): ...
def debug_numeric_summary(input: Any, device_name: str = ..., tensor_name: str = ..., debug_urls: Any = ..., lower_bound: Any = ..., upper_bound: Any = ..., mute_if_healthy: bool = ..., gated_grpc: bool = ..., name: Optional[Any] = ...): ...

DebugNumericSummary: Any

def debug_numeric_summary_eager_fallback(input: Any, device_name: Any, tensor_name: Any, debug_urls: Any, lower_bound: Any, upper_bound: Any, mute_if_healthy: Any, gated_grpc: Any, name: Any, ctx: Any): ...
def debug_numeric_summary_v2(input: Any, output_dtype: Any = ..., tensor_debug_mode: int = ..., tensor_id: int = ..., name: Optional[Any] = ...): ...

DebugNumericSummaryV2: Any

def debug_numeric_summary_v2_eager_fallback(input: Any, output_dtype: Any, tensor_debug_mode: Any, tensor_id: Any, name: Any, ctx: Any): ...
