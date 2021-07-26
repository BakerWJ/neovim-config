import gast
from typing import Any, Optional

class PrettyPrinter(gast.NodeVisitor):
    indent_lvl: int = ...
    result: str = ...
    color: Any = ...
    noanno: Any = ...
    def __init__(self, color: Any, noanno: Any) -> None: ...
    def generic_visit(self, node: Any, name: Optional[Any] = ...) -> None: ...

def fmt(node: Any, color: bool = ..., noanno: bool = ...): ...
