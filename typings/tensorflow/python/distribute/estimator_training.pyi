from tensorflow.python.distribute import multi_worker_util as multi_worker_util
from tensorflow.python.training import server_lib as server_lib
from typing import Any

CHIEF: Any
EVALUATOR: Any
PS: Any
WORKER: Any

def init_run_config(config: Any, tf_config: Any) -> None: ...
def should_run_distribute_coordinator(config: Any): ...
def train_and_evaluate(estimator: Any, train_spec: Any, eval_spec: Any, executor_cls: Any) -> None: ...
def estimator_train(estimator: Any, train_distributed_fn: Any, hooks: Any): ...
def estimator_evaluate(estimator: Any, evaluate_distributed_fn: Any, hooks: Any): ...
