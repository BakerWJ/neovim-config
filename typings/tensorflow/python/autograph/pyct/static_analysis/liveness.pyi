from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, transformer as transformer
from tensorflow.python.autograph.pyct.static_analysis import annos as annos
from typing import Any

class Analyzer(cfg.GraphVisitor):
    extra_gen: Any = ...
    def __init__(self, graph: Any) -> None: ...
    def init_state(self, _: Any): ...
    def visit_node(self, node: Any): ...

class WholeTreeAnalyzer(transformer.Base):
    graphs: Any = ...
    current_analyzer: Any = ...
    analyzers: Any = ...
    def __init__(self, source_info: Any, graphs: Any) -> None: ...
    def visit_FunctionDef(self, node: Any): ...

class Annotator(transformer.Base):
    cross_function_analyzer: Any = ...
    current_analyzer: Any = ...
    def __init__(self, source_info: Any, cross_function_analyzer: Any) -> None: ...
    def visit(self, node: Any): ...
    def visit_FunctionDef(self, node: Any): ...
    def visit_If(self, node: Any): ...
    def visit_For(self, node: Any): ...
    def visit_While(self, node: Any): ...
    def visit_Try(self, node: Any): ...
    def visit_ExceptHandler(self, node: Any): ...
    def visit_With(self, node: Any): ...
    def visit_Expr(self, node: Any): ...

def resolve(node: Any, source_info: Any, graphs: Any): ...