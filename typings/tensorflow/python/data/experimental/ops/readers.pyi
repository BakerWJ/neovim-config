from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import error_ops as error_ops, parsing_ops as parsing_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert, nest as nest
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops, io_ops as io_ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def make_tf_record_dataset(file_pattern: Any, batch_size: Any, parser_fn: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: Optional[Any] = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ..., num_parallel_parser_calls: Optional[Any] = ..., drop_final_batch: bool = ...): ...
def make_csv_dataset_v2(file_pattern: Any, batch_size: Any, column_names: Optional[Any] = ..., column_defaults: Optional[Any] = ..., label_name: Optional[Any] = ..., select_columns: Optional[Any] = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., header: bool = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ..., sloppy: bool = ..., num_rows_for_inference: int = ..., compression_type: Optional[Any] = ..., ignore_errors: bool = ...): ...
def make_csv_dataset_v1(file_pattern: Any, batch_size: Any, column_names: Optional[Any] = ..., column_defaults: Optional[Any] = ..., label_name: Optional[Any] = ..., select_columns: Optional[Any] = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., header: bool = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Optional[Any] = ..., num_parallel_reads: Optional[Any] = ..., sloppy: bool = ..., num_rows_for_inference: int = ..., compression_type: Optional[Any] = ..., ignore_errors: bool = ...): ...

class CsvDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, filenames: Any, record_defaults: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., header: bool = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Optional[Any] = ...) -> None: ...
    @property
    def element_spec(self): ...

class CsvDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames: Any, record_defaults: Any, compression_type: Optional[Any] = ..., buffer_size: Optional[Any] = ..., header: bool = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Optional[Any] = ...) -> None: ...

def make_batched_features_dataset_v2(file_pattern: Any, batch_size: Any, features: Any, reader: Optional[Any] = ..., label_key: Optional[Any] = ..., reader_args: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Optional[Any] = ..., reader_num_threads: Optional[Any] = ..., parser_num_threads: Optional[Any] = ..., sloppy_ordering: bool = ..., drop_final_batch: bool = ...): ...
def make_batched_features_dataset_v1(file_pattern: Any, batch_size: Any, features: Any, reader: Optional[Any] = ..., label_key: Optional[Any] = ..., reader_args: Optional[Any] = ..., num_epochs: Optional[Any] = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Optional[Any] = ..., prefetch_buffer_size: Optional[Any] = ..., reader_num_threads: Optional[Any] = ..., parser_num_threads: Optional[Any] = ..., sloppy_ordering: bool = ..., drop_final_batch: bool = ...): ...

class SqlDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, driver_name: Any, data_source_name: Any, query: Any, output_types: Any): ...
    @property
    def element_spec(self): ...

class SqlDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, driver_name: Any, data_source_name: Any, query: Any, output_types: Any) -> None: ...
CsvDataset = CsvDatasetV2
SqlDataset = SqlDatasetV2
make_batched_features_dataset = make_batched_features_dataset_v2
make_csv_dataset = make_csv_dataset_v2
CsvDataset = CsvDatasetV1
SqlDataset = SqlDatasetV1
make_batched_features_dataset = make_batched_features_dataset_v1
make_csv_dataset = make_csv_dataset_v1
