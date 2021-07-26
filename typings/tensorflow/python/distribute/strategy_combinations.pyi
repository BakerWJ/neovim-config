from tensorflow.python import tf2 as tf2
from tensorflow.python.distribute import central_storage_strategy as central_storage_strategy, combinations as combinations, distribution_strategy_context as distribution_strategy_context
from tensorflow.python.distribute.cluster_resolver import tpu_cluster_resolver as tpu_cluster_resolver
from tensorflow.python.eager import context as context, remote as remote
from tensorflow.python.framework import config as config
from tensorflow.python.platform import flags as flags
from tensorflow.python.tpu import tpu_strategy_util as tpu_strategy_util
from tensorflow.python.training import adagrad as adagrad, adam as adam, ftrl as ftrl, gradient_descent as gradient_descent, rmsprop as rmsprop
from typing import Any

FLAGS: Any
default_strategy: Any
one_device_strategy: Any
one_device_strategy_gpu: Any
one_device_strategy_on_worker_1: Any
one_device_strategy_gpu_on_worker_1: Any
tpu_strategy: Any
tpu_strategy_one_step: Any
tpu_strategy_one_core: Any
tpu_strategy_one_step_one_core: Any
cloud_tpu_strategy: Any
mirrored_strategy_with_one_cpu: Any
mirrored_strategy_with_one_gpu: Any
mirrored_strategy_with_gpu_and_cpu: Any
mirrored_strategy_with_two_gpus: Any
mirrored_strategy_with_cpu_1_and_2: Any
central_storage_strategy_with_two_gpus: Any
central_storage_strategy_with_gpu_and_cpu: Any
gradient_descent_optimizer_v1_fn: Any
adagrad_optimizer_v1_fn: Any
adam_optimizer_v1_fn: Any
ftrl_optimizer_v1_fn: Any
rmsprop_optimizer_v1_fn: Any
optimizers_v1: Any
adadelta_optimizer_keras_v2_fn: Any
adagrad_optimizer_keras_v2_fn: Any
adam_optimizer_keras_v2_fn: Any
adamax_optimizer_keras_v2_fn: Any
nadam_optimizer_keras_v2_fn: Any
ftrl_optimizer_keras_v2_fn: Any
gradient_descent_optimizer_keras_v2_fn: Any
rmsprop_optimizer_keras_v2_fn: Any
optimizers_v2: Any
optimizers_v1_and_v2: Any
graph_and_eager_modes: Any

def set_virtual_cpus_to_at_least(num_virtual_cpus: Any) -> None: ...
def distributions_and_v1_optimizers(): ...
def distributions_and_v2_optimizers(): ...
def distributions_and_v1_and_v2_optimizers(): ...

strategies_minus_tpu: Any
strategies_minus_default_and_tpu: Any
tpu_strategies: Any
all_strategies_minus_default: Any
all_strategies: Any
multidevice_strategies: Any

def strategy_minus_tpu_combinations(): ...
def tpu_strategy_combinations(): ...
def all_strategy_combinations(): ...
def all_strategy_minus_default_and_tpu_combinations(): ...
def all_strategy_combinations_minus_default(): ...
