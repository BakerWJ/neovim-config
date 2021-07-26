from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.python import _dtypes, pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class DType(_dtypes.DType):
    @property
    def base_dtype(self): ...
    @property
    def real_dtype(self): ...
    @property
    def as_numpy_dtype(self): ...
    @property
    def min(self): ...
    @property
    def max(self): ...
    @property
    def limits(self, clip_negative: bool = ...): ...
    def is_compatible_with(self, other: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    def __reduce__(self): ...

dtype_range: Any
resource: Any
variant: Any
float16: Any
half = float16
float32: Any
float64: Any
double = float64
int32: Any
uint8: Any
uint16: Any
uint32: Any
uint64: Any
int16: Any
int8: Any
string: Any
complex64: Any
complex128: Any
int64: Any
bool: Any
qint8: Any
quint8: Any
qint16: Any
quint16: Any
qint32: Any
resource_ref: Any
variant_ref: Any
bfloat16: Any
float16_ref: Any
half_ref = float16_ref
float32_ref: Any
float64_ref: Any
double_ref = float64_ref
int32_ref: Any
uint32_ref: Any
uint8_ref: Any
uint16_ref: Any
int16_ref: Any
int8_ref: Any
string_ref: Any
complex64_ref: Any
complex128_ref: Any
int64_ref: Any
uint64_ref: Any
bool_ref: Any
qint8_ref: Any
quint8_ref: Any
qint16_ref: Any
quint16_ref: Any
qint32_ref: Any
bfloat16_ref: Any
np_resource: Any
TF_VALUE_DTYPES: Any
QUANTIZED_DTYPES: Any

def as_dtype(type_value: Any): ...
