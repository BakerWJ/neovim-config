from tensorflow.core.framework.summary_pb2 import Summary as Summary, SummaryDescription as SummaryDescription
from tensorflow.core.util.event_pb2 import Event as Event, SessionLog as SessionLog, TaggedRunMetadata as TaggedRunMetadata
from tensorflow.python.summary.writer.writer import FileWriter as FileWriter
from tensorflow.python.summary.writer.writer_cache import FileWriterCache as FileWriterCache
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def scalar(name: Any, tensor: Any, collections: Optional[Any] = ..., family: Optional[Any] = ...): ...
def image(name: Any, tensor: Any, max_outputs: int = ..., collections: Optional[Any] = ..., family: Optional[Any] = ...): ...
def histogram(name: Any, values: Any, collections: Optional[Any] = ..., family: Optional[Any] = ...): ...
def audio(name: Any, tensor: Any, sample_rate: Any, max_outputs: int = ..., collections: Optional[Any] = ..., family: Optional[Any] = ...): ...
def text(name: Any, tensor: Any, collections: Optional[Any] = ...): ...
def tensor_summary(name: Any, tensor: Any, summary_description: Optional[Any] = ..., collections: Optional[Any] = ..., summary_metadata: Optional[Any] = ..., family: Optional[Any] = ..., display_name: Optional[Any] = ...): ...
def merge(inputs: Any, collections: Optional[Any] = ..., name: Optional[Any] = ...): ...
def merge_all(key: Any = ..., scope: Optional[Any] = ..., name: Optional[Any] = ...): ...
def get_summary_description(node_def: Any): ...