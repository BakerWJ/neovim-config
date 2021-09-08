import argparse
from tensorflow.lite.python import lite as lite, lite_constants as lite_constants
from tensorflow.lite.toco.logging import gen_html as gen_html
from tensorflow.python import keras as keras, tf2 as tf2
from tensorflow.python.platform import app as app
from typing import Any, Optional

class _ParseExperimentalNewConverter(argparse.Action):
    def __init__(self, option_strings: Any, dest: Any, nargs: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def __call__(self, parser: Any, namespace: Any, values: Any, option_string: Optional[Any] = ...) -> None: ...

def run_main(_: Any) -> None: ...
def main() -> None: ...