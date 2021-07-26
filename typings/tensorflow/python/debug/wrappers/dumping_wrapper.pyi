from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.debug.lib import debug_data as debug_data
from tensorflow.python.debug.wrappers import framework as framework
from tensorflow.python.platform import gfile as gfile
from typing import Any, Optional

class DumpingDebugWrapperSession(framework.NonInteractiveDebugWrapperSession):
    def __init__(self, sess: Any, session_root: Any, watch_fn: Optional[Any] = ..., thread_name_filter: Optional[Any] = ..., pass_through_operrors: Optional[Any] = ..., log_usage: bool = ...) -> None: ...
    def prepare_run_debug_urls(self, fetches: Any, feed_dict: Any): ...
