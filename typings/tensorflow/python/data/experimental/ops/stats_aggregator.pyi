from tensorflow.python.ops import summary_ops_v2 as summary_ops_v2
from tensorflow.python.util.tf_export import tf_export as tf_export

class StatsAggregatorV2:
    def __init__(self) -> None: ...

class StatsAggregatorV1:
    def __init__(self) -> None: ...
    def get_summary(self): ...
StatsAggregator = StatsAggregatorV1
