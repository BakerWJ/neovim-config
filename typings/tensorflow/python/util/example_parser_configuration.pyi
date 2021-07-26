from tensorflow.core.example import example_parser_configuration_pb2 as example_parser_configuration_pb2
from tensorflow.python.framework import tensor_shape as tensor_shape, tensor_util as tensor_util
from typing import Any

def extract_example_parser_configuration(parse_example_op: Any, sess: Any): ...
