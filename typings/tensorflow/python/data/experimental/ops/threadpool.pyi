from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.eager import context as context
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from typing import Any, Optional

class PrivateThreadPool:
    def __init__(self, num_threads: Any, display_name: Optional[Any] = ..., max_intra_op_parallelism: int = ...) -> None: ...

class _ThreadPoolDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset: Any, thread_pool: Any) -> None: ...

def override_threadpool(dataset: Any, thread_pool: Any): ...
