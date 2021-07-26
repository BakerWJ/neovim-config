from tensorflow.core.protobuf import queue_runner_pb2 as queue_runner_pb2
from tensorflow.python.client import session as session
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class QueueRunner:
    def __init__(self, queue: Optional[Any] = ..., enqueue_ops: Optional[Any] = ..., close_op: Optional[Any] = ..., cancel_op: Optional[Any] = ..., queue_closed_exception_types: Optional[Any] = ..., queue_runner_def: Optional[Any] = ..., import_scope: Optional[Any] = ...) -> None: ...
    @property
    def queue(self): ...
    @property
    def enqueue_ops(self): ...
    @property
    def close_op(self): ...
    @property
    def cancel_op(self): ...
    @property
    def queue_closed_exception_types(self): ...
    @property
    def exceptions_raised(self): ...
    @property
    def name(self): ...
    def create_threads(self, sess: Any, coord: Optional[Any] = ..., daemon: bool = ..., start: bool = ...): ...
    def to_proto(self, export_scope: Optional[Any] = ...): ...
    @staticmethod
    def from_proto(queue_runner_def: Any, import_scope: Optional[Any] = ...): ...

def add_queue_runner(qr: Any, collection: Any = ...) -> None: ...
def start_queue_runners(sess: Optional[Any] = ..., coord: Optional[Any] = ..., daemon: bool = ..., start: bool = ..., collection: Any = ...): ...
