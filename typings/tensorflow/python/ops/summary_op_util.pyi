from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import tf_logging as tf_logging
from typing import Any, Optional

def collect(val: Any, collections: Any, default_collections: Any) -> None: ...
def clean_tag(name: Any): ...
def summary_scope(name: Any, family: Optional[Any] = ..., default_name: Optional[Any] = ..., values: Optional[Any] = ...) -> None: ...
