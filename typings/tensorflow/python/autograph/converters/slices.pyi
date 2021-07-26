from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.lang import directives as directives
from tensorflow.python.autograph.pyct import templates as templates
from typing import Any

class SliceTransformer(converter.Base):
    def visit_Assign(self, node: Any): ...
    def visit_Subscript(self, node: Any): ...

def transform(node: Any, ctx: Any): ...
