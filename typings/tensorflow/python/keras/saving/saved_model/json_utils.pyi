import json
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.util import serialization as serialization
from typing import Any

class Encoder(json.JSONEncoder):
    def default(self, obj: Any): ...
    def encode(self, obj: Any): ...

def decode(json_string: Any): ...
