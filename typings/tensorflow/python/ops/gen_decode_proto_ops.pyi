from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_DecodeProtoV2Output = namedtuple('DecodeProtoV2', ['sizes', 'values'])

def decode_proto_v2(bytes: Any, message_type: Any, field_names: Any, output_types: Any, descriptor_source: str = ..., message_format: str = ..., sanitize: bool = ..., name: Optional[Any] = ...): ...

DecodeProtoV2: Any

def decode_proto_v2_eager_fallback(bytes: Any, message_type: Any, field_names: Any, output_types: Any, descriptor_source: Any, message_format: Any, sanitize: Any, name: Any, ctx: Any): ...
