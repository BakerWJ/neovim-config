from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.ops import state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.training import checkpoint_ops as checkpoint_ops, checkpoint_utils as checkpoint_utils
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

class VocabInfo:
    def __new__(cls, new_vocab: Any, new_vocab_size: Any, num_oov_buckets: Any, old_vocab: Any, old_vocab_size: int = ..., backup_initializer: Optional[Any] = ..., axis: int = ...): ...

def warm_start(ckpt_to_initialize_from: Any, vars_to_warm_start: str = ..., var_name_to_vocab_info: Optional[Any] = ..., var_name_to_prev_var_name: Optional[Any] = ...) -> None: ...
