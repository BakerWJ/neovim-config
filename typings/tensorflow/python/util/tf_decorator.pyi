from tensorflow.python.util import tf_stack as tf_stack
from typing import Any, Optional

def make_decorator(target: Any, decorator_func: Any, decorator_name: Optional[Any] = ..., decorator_doc: str = ..., decorator_argspec: Optional[Any] = ...): ...
def rewrap(decorator_func: Any, previous_target: Any, new_target: Any): ...
def unwrap(maybe_tf_decorator: Any): ...

class TFDecorator:
    __name__: Any = ...
    __qualname__: Any = ...
    __doc__: Any = ...
    def __init__(self, decorator_name: Any, target: Any, decorator_doc: str = ..., decorator_argspec: Optional[Any] = ...) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    @property
    def decorated_target(self): ...
    @decorated_target.setter
    def decorated_target(self, decorated_target: Any) -> None: ...
    @property
    def decorator_name(self): ...
    @property
    def decorator_doc(self): ...
    @property
    def decorator_argspec(self): ...