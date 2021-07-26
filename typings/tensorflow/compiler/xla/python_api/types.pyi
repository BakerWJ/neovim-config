from collections import namedtuple
from tensorflow.compiler.xla import xla_data_pb2 as xla_data_pb2
from tensorflow.python.framework import dtypes as dtypes
from typing import Any

TypeConversionRecord = namedtuple('TypeConversionRecord', ['primitive_type', 'numpy_dtype', 'literal_field_name', 'literal_field_type'])
MAP_XLA_TYPE_TO_RECORD: Any
MAP_DTYPE_TO_RECORD: Any
