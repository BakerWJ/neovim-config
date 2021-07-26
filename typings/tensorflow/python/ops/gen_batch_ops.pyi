from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_BatchOutput = namedtuple('Batch', ['batched_tensors', 'batch_index', 'id'])

def batch(in_tensors: Any, num_batch_threads: Any, max_batch_size: Any, batch_timeout_micros: Any, grad_timeout_micros: Any, max_enqueued_batches: int = ..., allowed_batch_sizes: Any = ..., container: str = ..., shared_name: str = ..., batching_queue: str = ..., name: Optional[Any] = ...): ...

Batch: Any

def batch_eager_fallback(in_tensors: Any, num_batch_threads: Any, max_batch_size: Any, batch_timeout_micros: Any, grad_timeout_micros: Any, max_enqueued_batches: Any, allowed_batch_sizes: Any, container: Any, shared_name: Any, batching_queue: Any, name: Any, ctx: Any): ...
def batch_function(in_tensors: Any, captured_tensors: Any, f: Any, num_batch_threads: Any, max_batch_size: Any, batch_timeout_micros: Any, Tout: Any, max_enqueued_batches: int = ..., allowed_batch_sizes: Any = ..., container: str = ..., shared_name: str = ..., batching_queue: str = ..., name: Optional[Any] = ...): ...

BatchFunction: Any

def batch_function_eager_fallback(in_tensors: Any, captured_tensors: Any, f: Any, num_batch_threads: Any, max_batch_size: Any, batch_timeout_micros: Any, Tout: Any, max_enqueued_batches: Any, allowed_batch_sizes: Any, container: Any, shared_name: Any, batching_queue: Any, name: Any, ctx: Any): ...
def unbatch(batched_tensor: Any, batch_index: Any, id: Any, timeout_micros: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

Unbatch: Any

def unbatch_eager_fallback(batched_tensor: Any, batch_index: Any, id: Any, timeout_micros: Any, container: Any, shared_name: Any, name: Any, ctx: Any): ...
def unbatch_grad(original_input: Any, batch_index: Any, grad: Any, id: Any, container: str = ..., shared_name: str = ..., name: Optional[Any] = ...): ...

UnbatchGrad: Any

def unbatch_grad_eager_fallback(original_input: Any, batch_index: Any, grad: Any, id: Any, container: Any, shared_name: Any, name: Any, ctx: Any): ...
