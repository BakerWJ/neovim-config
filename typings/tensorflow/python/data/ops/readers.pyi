from tensorflow.python import tf2 as tf2
from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class _TextLineDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class TextLineDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...): ...
    @property
    def element_spec(self): ...

class TextLineDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...) -> None: ...

class _TFRecordDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class ParallelInterleaveDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset: Any, map_func: Any, cycle_length: Any, block_length: Any, sloppy: Any, buffer_output_elements: Any, prefetch_input_elements: Any) -> None: ...
    @property
    def element_spec(self): ...

class TFRecordDatasetV2(dataset_ops.DatasetV2):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...): ...
    @property
    def element_spec(self): ...

class TFRecordDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...) -> None: ...

class _FixedLengthRecordDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, record_bytes: Any, header_bytes: Optional[Any] = ..., footer_bytes: Optional[Any] = ..., buffer_size: Optional[Any] = ..., compression_type: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class FixedLengthRecordDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, record_bytes: Any, header_bytes: Optional[Any] = ..., footer_bytes: Optional[Any] = ..., buffer_size: Optional[Any] = ..., compression_type: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...): ...
    @property
    def element_spec(self): ...

class FixedLengthRecordDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames: Any, record_bytes: Any, header_bytes: Optional[Any] = ..., footer_bytes: Optional[Any] = ..., buffer_size: Optional[Any] = ..., compression_type: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ...) -> None: ...
FixedLengthRecordDataset = FixedLengthRecordDatasetV2
TFRecordDataset = TFRecordDatasetV2
TextLineDataset = TextLineDatasetV2
FixedLengthRecordDataset = FixedLengthRecordDatasetV1
TFRecordDataset = TFRecordDatasetV1
TextLineDataset = TextLineDatasetV1
