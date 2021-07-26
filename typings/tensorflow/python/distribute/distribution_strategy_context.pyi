from tensorflow.python.framework import ops as ops
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

distribute_lib: Any

class _ThreadMode:
    strategy: Any = ...
    cross_replica_context: Any = ...
    replica_context: Any = ...
    def __init__(self, dist: Any, cross: Any, replica: Any) -> None: ...

class _CrossReplicaThreadMode(_ThreadMode):
    def __init__(self, strategy: Any) -> None: ...

class _InReplicaThreadMode(_ThreadMode):
    def __init__(self, replica_ctx: Any) -> None: ...

class _DefaultReplicaThreadMode(_ThreadMode):
    def __init__(self) -> None: ...

def get_replica_context(): ...
def get_cross_replica_context(): ...
def in_cross_replica_context(): ...
def get_strategy(): ...
def has_strategy(): ...
def get_strategy_and_replica_context(): ...
def experimental_set_strategy(strategy: Any) -> None: ...
def enter_or_assert_strategy(strategy: Any) -> None: ...
get_distribution_strategy = get_strategy
has_distribution_strategy = has_strategy
