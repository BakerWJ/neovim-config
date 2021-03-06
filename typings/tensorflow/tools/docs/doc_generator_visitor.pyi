from tensorflow.python.util import tf_export as tf_export, tf_inspect as tf_inspect
from typing import Any

class DocGeneratorVisitor:
    def __init__(self, root_name: str = ...) -> None: ...
    def set_root_name(self, root_name: Any) -> None: ...
    @property
    def index(self): ...
    @property
    def tree(self): ...
    @property
    def reverse_index(self): ...
    @property
    def duplicate_of(self): ...
    @property
    def duplicates(self): ...
    def __call__(self, parent_name: Any, parent: Any, children: Any) -> None: ...
