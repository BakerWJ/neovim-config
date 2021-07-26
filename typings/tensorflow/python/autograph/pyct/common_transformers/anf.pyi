from tensorflow.python.autograph.pyct import gast_util as gast_util, templates as templates, transformer as transformer
from typing import Any, Optional

class DummyGensym:
    def __init__(self, ctx: Any) -> None: ...
    def new_name(self, stem: str = ...): ...

REPLACE: Any
LEAVE: Any
ANY: Any

class ASTEdgePattern:
    def matches(self, parent: Any, field: Any, child: Any): ...

class AnfTransformer(transformer.Base):
    def __init__(self, ctx: Any, config: Any, gensym_source: Optional[Any] = ...) -> None: ...
    def visit_Return(self, node: Any): ...
    def visit_Delete(self, node: Any): ...
    def visit_Assign(self, node: Any): ...
    def visit_AugAssign(self, node: Any): ...
    def visit_Print(self, node: Any): ...
    def visit_For(self, node: Any): ...
    def visit_AsyncFor(self, node: Any): ...
    def visit_While(self, node: Any): ...
    def visit_If(self, node: Any): ...
    def visit_With(self, node: Any): ...
    def visit_AsyncWith(self, node: Any): ...
    def visit_Raise(self, node: Any): ...
    def visit_Assert(self, node: Any): ...
    def visit_Exec(self, node: Any): ...
    def visit_Expr(self, node: Any): ...
    def visit_BoolOp(self, node: Any): ...
    def visit_BinOp(self, node: Any): ...
    def visit_UnaryOp(self, node: Any): ...
    def visit_Lambda(self, node: Any): ...
    def visit_IfExp(self, node: Any): ...
    def visit_Dict(self, node: Any): ...
    def visit_Set(self, node: Any): ...
    def visit_ListComp(self, node: Any) -> None: ...
    def visit_SetComp(self, node: Any) -> None: ...
    def visit_DictComp(self, node: Any) -> None: ...
    def visit_GeneratorExp(self, node: Any) -> None: ...
    def visit_Await(self, node: Any): ...
    def visit_Yield(self, node: Any): ...
    def visit_YieldFrom(self, node: Any): ...
    def visit_Compare(self, node: Any): ...
    def visit_Call(self, node: Any): ...
    def visit_Repr(self, node: Any): ...
    def visit_FormattedValue(self, node: Any): ...
    def visit_JoinedStr(self, node: Any): ...
    def visit_Attribute(self, node: Any): ...
    def visit_Subscript(self, node: Any): ...
    def visit_List(self, node: Any): ...
    def visit_Tuple(self, node: Any): ...

def transform(node: Any, ctx: Any, config: Optional[Any] = ..., gensym_source: Optional[Any] = ...): ...
