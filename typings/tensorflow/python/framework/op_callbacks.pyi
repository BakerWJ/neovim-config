from tensorflow.python.eager import context as context, execute as execute
from typing import Any, Optional

def add_op_callback(callback_fn: Any) -> None: ...
def should_invoke_op_callbacks(): ...
def remove_op_callback(op_callback: Any) -> None: ...
def clear_op_callbacks() -> None: ...
def invoke_op_callbacks(op_type: Any, inputs: Any, attrs: Any, outputs: Any, op_name: Optional[Any] = ..., graph: Optional[Any] = ...): ...
