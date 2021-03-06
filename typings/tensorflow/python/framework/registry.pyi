from tensorflow.python.util import compat as compat, tf_stack as tf_stack
from typing import Any, Optional

class Registry:
    def __init__(self, name: Any) -> None: ...
    def register(self, candidate: Any, name: Optional[Any] = ...) -> None: ...
    def list(self): ...
    def lookup(self, name: Any): ...
