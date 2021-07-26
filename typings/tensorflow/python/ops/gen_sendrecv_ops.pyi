from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def recv(tensor_type: Any, tensor_name: Any, send_device: Any, send_device_incarnation: Any, recv_device: Any, client_terminated: bool = ..., name: Optional[Any] = ...): ...

Recv: Any

def recv_eager_fallback(tensor_type: Any, tensor_name: Any, send_device: Any, send_device_incarnation: Any, recv_device: Any, client_terminated: Any, name: Any, ctx: Any): ...
def send(tensor: Any, tensor_name: Any, send_device: Any, send_device_incarnation: Any, recv_device: Any, client_terminated: bool = ..., name: Optional[Any] = ...): ...

Send: Any

def send_eager_fallback(tensor: Any, tensor_name: Any, send_device: Any, send_device_incarnation: Any, recv_device: Any, client_terminated: Any, name: Any, ctx: Any): ...
