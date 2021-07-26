from collections import namedtuple
from tensorflow.python.util import tf_export as tf_export
from typing import Any

DocSource = namedtuple('DocSource', ['docstring', 'docstring_module_name'])

def get_doc_sources(api_name: Any): ...
