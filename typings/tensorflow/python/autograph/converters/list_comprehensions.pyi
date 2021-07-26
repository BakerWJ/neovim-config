from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import templates as templates
from typing import Any

class ListCompTransformer(converter.Base):
    def visit_Assign(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
