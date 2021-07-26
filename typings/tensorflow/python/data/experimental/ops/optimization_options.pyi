import enum
from tensorflow.python.data.util import options as options
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class _AutotuneAlgorithm(enum.Enum):
    HILL_CLIMB: int = ...
    GRADIENT_DESCENT: int = ...

class MapVectorizationOptions(options.OptionsBase):
    enabled: Any = ...
    use_choose_fastest: Any = ...

class OptimizationOptions(options.OptionsBase):
    apply_default_optimizations: Any = ...
    autotune: Any = ...
    autotune_buffers: Any = ...
    autotune_cpu_budget: Any = ...
    filter_fusion: Any = ...
    filter_with_random_uniform_fusion: Any = ...
    hoist_random_uniform: Any = ...
    map_and_batch_fusion: Any = ...
    map_and_filter_fusion: Any = ...
    map_fusion: Any = ...
    map_parallelization: Any = ...
    map_vectorization: Any = ...
    noop_elimination: Any = ...
    parallel_batch: Any = ...
    shuffle_and_repeat_fusion: Any = ...
