from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import templates as templates
from typing import Any

class ConditionalExpressionTransformer(converter.Base):
    def visit_IfExp(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
