from tensorflow.python.util import tf_inspect as tf_inspect
from typing import Any

class PublicAPIVisitor:
    def __init__(self, visitor: Any) -> None: ...
    @property
    def private_map(self): ...
    @property
    def do_not_descend_map(self): ...
    def set_root_name(self, root_name: Any) -> None: ...
    def __call__(self, path: Any, parent: Any, children: Any) -> None: ...
