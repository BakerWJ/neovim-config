import threading
from tensorflow.python.distribute.cluster_resolver import tpu_cluster_resolver as tpu_cluster_resolver
from tensorflow.python.training import session_run_hook as session_run_hook
from typing import Any

class CloudTPUPreemptedHook(session_run_hook.SessionRunHook):
    def __init__(self, cluster: Any) -> None: ...
    def after_create_session(self, session: Any, coord: Any) -> None: ...
    def end(self, session: Any) -> None: ...

class _TPUPollingThread(threading.Thread):
    daemon: bool = ...
    def __init__(self, cluster: Any, session: Any) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...
