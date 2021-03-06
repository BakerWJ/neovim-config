from tensorflow.python.ops.gen_parsing_ops import *
from tensorflow.python.framework import ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_parsing_ops as gen_parsing_ops, math_ops as math_ops, parsing_config as parsing_config
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

VarLenFeature = parsing_config.VarLenFeature
RaggedFeature = parsing_config.RaggedFeature
SparseFeature = parsing_config.SparseFeature
FixedLenFeature = parsing_config.FixedLenFeature
FixedLenSequenceFeature = parsing_config.FixedLenSequenceFeature

def parse_example_v2(serialized: Any, features: Any, example_names: Optional[Any] = ..., name: Optional[Any] = ...): ...
def parse_example(serialized: Any, features: Any, name: Optional[Any] = ..., example_names: Optional[Any] = ...): ...
def parse_single_example(serialized: Any, features: Any, name: Optional[Any] = ..., example_names: Optional[Any] = ...): ...
def parse_single_example_v2(serialized: Any, features: Any, example_names: Optional[Any] = ..., name: Optional[Any] = ...): ...
def parse_sequence_example(serialized: Any, context_features: Optional[Any] = ..., sequence_features: Optional[Any] = ..., example_names: Optional[Any] = ..., name: Optional[Any] = ...): ...
def parse_single_sequence_example(serialized: Any, context_features: Optional[Any] = ..., sequence_features: Optional[Any] = ..., example_name: Optional[Any] = ..., name: Optional[Any] = ...): ...
def decode_raw(input_bytes: Any, out_type: Any, little_endian: bool = ..., fixed_length: Optional[Any] = ..., name: Optional[Any] = ...): ...
def decode_raw_v1(input_bytes: Optional[Any] = ..., out_type: Optional[Any] = ..., little_endian: bool = ..., name: Optional[Any] = ..., bytes: Optional[Any] = ...): ...
def decode_csv(records: Any, record_defaults: Any, field_delim: str = ..., use_quote_delim: bool = ..., name: Optional[Any] = ..., na_value: str = ..., select_cols: Optional[Any] = ...): ...
def decode_csv_v2(records: Any, record_defaults: Any, field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Optional[Any] = ..., name: Optional[Any] = ...): ...
