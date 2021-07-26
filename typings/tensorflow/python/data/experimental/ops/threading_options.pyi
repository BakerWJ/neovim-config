from tensorflow.python.data.util import options as options
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class ThreadingOptions(options.OptionsBase):
    max_intra_op_parallelism: Any = ...
    private_threadpool_size: Any = ...
