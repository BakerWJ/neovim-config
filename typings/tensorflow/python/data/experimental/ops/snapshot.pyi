from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, random_seed as random_seed
from typing import Any, Optional

COMPRESSION_GZIP: str
COMPRESSION_SNAPPY: str
COMPRESSION_NONE: Any

class _SnapshotDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, path: Any, compression: Optional[Any] = ..., reader_path_prefix: Optional[Any] = ..., writer_path_prefix: Optional[Any] = ..., shard_size_bytes: Optional[Any] = ..., pending_snapshot_expiry_seconds: Optional[Any] = ..., num_reader_threads: Optional[Any] = ..., reader_buffer_size: Optional[Any] = ..., num_writer_threads: Optional[Any] = ..., writer_buffer_size: Optional[Any] = ..., shuffle_on_read: Optional[Any] = ..., shuffle_seed: Optional[Any] = ..., mode: Optional[Any] = ..., snapshot_name: Optional[Any] = ...) -> None: ...

def snapshot(path: Any, compression: Optional[Any] = ..., reader_path_prefix: Optional[Any] = ..., writer_path_prefix: Optional[Any] = ..., shard_size_bytes: Optional[Any] = ..., pending_snapshot_expiry_seconds: Optional[Any] = ..., num_reader_threads: Optional[Any] = ..., reader_buffer_size: Optional[Any] = ..., num_writer_threads: Optional[Any] = ..., writer_buffer_size: Optional[Any] = ..., shuffle_on_read: Optional[Any] = ..., shuffle_seed: Optional[Any] = ..., mode: Optional[Any] = ..., snapshot_name: Optional[Any] = ...): ...
