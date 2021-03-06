from tensorflow.python.autograph import operators as operators, utils as utils
from tensorflow.python.autograph.core import config as config, converter as converter, function_wrappers as function_wrappers, naming as naming
from tensorflow.python.autograph.lang import special_functions as special_functions
from tensorflow.python.autograph.pyct import loader as loader, origin_info as origin_info, parser as parser, pretty_printer as pretty_printer, transformer as transformer
from tensorflow.python.platform import test as test
from typing import Any

def whitelist(entity: Any) -> None: ...
def is_inside_generated_code(): ...

class TestCase(test.TestCase):
    def assertPrints(self, expected_result: Any) -> None: ...
    dynamic_calls: Any = ...
    def compiled(self, node: Any, namespace: Any, symbols: Any = ...): ...
    def converted(self, entity: Any, converter_module: Any, namespace: Any, tf_symbols: Any = ...) -> None: ...
    def make_fake_mod(self, name: Any, *symbols: Any): ...
    def attach_namespace(self, module: Any, **ns: Any) -> None: ...
    def prepare(self, test_fn: Any, namespace: Any, recursive: bool = ...): ...
