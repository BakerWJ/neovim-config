import enum
from tensorflow.python.ops import variable_scope as variable_scope
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class ReduceOp(enum.Enum):
    SUM: str = ...
    MEAN: str = ...
    @staticmethod
    def from_variable_aggregation(aggregation: Any): ...
