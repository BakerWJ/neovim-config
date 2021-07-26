from tensorflow.python.distribute import multi_worker_util as multi_worker_util
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes
from tensorflow.python.keras.utils import mode_keys as mode_keys
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.training.tracking import tracking as tracking
from typing import Any

CKPT_SAVED_EPOCH: str
CKPT_SAVED_EPOCH_UNUSED_VALUE: int

def checkpoint_exists(filepath: Any): ...
def remove_checkpoint_if_exists(ckpt_dir: Any, filepath: Any): ...

class MultiWorkerTrainingState:
    def __init__(self, model: Any, original_filepath: Any) -> None: ...
    def back_up(self, epoch: Any) -> None: ...
    def restore(self): ...
    def delete_backup(self) -> None: ...
    def maybe_load_initial_epoch_from_ckpt(self, initial_epoch: Any, mode: Any): ...
    def untrack_vars(self) -> None: ...
