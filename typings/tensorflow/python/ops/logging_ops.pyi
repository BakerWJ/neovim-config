from tensorflow.python.ops.gen_logging_ops import *
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import gen_logging_ops as gen_logging_ops, string_ops as string_ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import nest as nest
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def Print(input_: Any, data: Any, message: Optional[Any] = ..., first_n: Optional[Any] = ..., summarize: Optional[Any] = ..., name: Optional[Any] = ...): ...
def print_v2(*inputs: Any, **kwargs: Any): ...
def histogram_summary(tag: Any, values: Any, collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
def image_summary(tag: Any, tensor: Any, max_images: int = ..., collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
def audio_summary(tag: Any, tensor: Any, sample_rate: Any, max_outputs: int = ..., collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
def merge_summary(inputs: Any, collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
def merge_all_summaries(key: Any = ...): ...
def get_summary_op(): ...
def scalar_summary(tags: Any, values: Any, collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
