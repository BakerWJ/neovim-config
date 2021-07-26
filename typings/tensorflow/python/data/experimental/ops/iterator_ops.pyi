from tensorflow.python.data.experimental.ops import distribute_options as distribute_options
from tensorflow.python.data.ops import iterator_ops as iterator_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, checkpoint_management as checkpoint_management, saver as saver_lib, session_run_hook as session_run_hook
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def make_saveable_from_iterator(iterator: Any, external_state_policy: str = ...): ...

class CheckpointInputPipelineHook(session_run_hook.SessionRunHook):
    def __init__(self, estimator: Any, external_state_policy: str = ...) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def before_run(self, run_context: Any): ...
    def after_run(self, run_context: Any, run_values: Any) -> None: ...
    def end(self, session: Any) -> None: ...

class _CustomSaver(saver_lib.Saver):
    def __init__(self, var_list: Any, latest_filename: Any, sharded: bool = ...) -> None: ...
    def save(self, sess: Any, save_path: Any, global_step: Optional[Any] = ..., latest_filename: Optional[Any] = ..., meta_graph_suffix: str = ..., write_meta_graph: bool = ..., write_state: bool = ..., strip_default_attrs: bool = ...): ...
