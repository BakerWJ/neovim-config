from tensorflow.python.data.experimental.ops import distribute as distribute
from tensorflow.python.data.experimental.ops.distribute_options import AutoShardPolicy as AutoShardPolicy
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import traverse as traverse
from tensorflow.python.framework import op_def_registry as op_def_registry, ops as ops
from typing import Any

def auto_shard_dataset(dataset: Any, num_shards: Any, index: Any): ...
