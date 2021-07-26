from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_GenerateVocabRemappingOutput = namedtuple('GenerateVocabRemapping', ['remapping', 'num_present'])

def generate_vocab_remapping(new_vocab_file: Any, old_vocab_file: Any, new_vocab_offset: Any, num_new_vocab: Any, old_vocab_size: int = ..., name: Optional[Any] = ...): ...

GenerateVocabRemapping: Any

def generate_vocab_remapping_eager_fallback(new_vocab_file: Any, old_vocab_file: Any, new_vocab_offset: Any, num_new_vocab: Any, old_vocab_size: Any, name: Any, ctx: Any): ...
def load_and_remap_matrix(ckpt_path: Any, old_tensor_name: Any, row_remapping: Any, col_remapping: Any, initializing_values: Any, num_rows: Any, num_cols: Any, max_rows_in_memory: int = ..., name: Optional[Any] = ...): ...

LoadAndRemapMatrix: Any

def load_and_remap_matrix_eager_fallback(ckpt_path: Any, old_tensor_name: Any, row_remapping: Any, col_remapping: Any, initializing_values: Any, num_rows: Any, num_cols: Any, max_rows_in_memory: Any, name: Any, ctx: Any): ...
