from tensorflow.python.data.experimental.ops import interleave_ops as interleave_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops, readers as readers
from tensorflow.python.framework import dtypes as dtypes, function as function, ops as ops
from tensorflow.python.ops import functional_ops as functional_ops
from typing import Any, Optional

def StreamingFilesDataset(files: Any, filetype: Optional[Any] = ..., file_reader_job: Optional[Any] = ..., worker_job: Optional[Any] = ..., num_epochs: Optional[Any] = ..., filename_shuffle_buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ..., batch_transfer_size: Optional[Any] = ..., sloppy: Optional[Any] = ...): ...
