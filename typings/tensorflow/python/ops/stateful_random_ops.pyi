import enum
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, gen_stateful_random_ops as gen_stateful_random_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, variables as variables
from tensorflow.python.training.tracking import tracking as tracking
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

MAX_INT64: Any
MIN_INT64: Any
UINT64_SPAN: Any
SEED_TYPE: str
SEED_MIN = MIN_INT64
SEED_MAX = MAX_INT64
SEED_UINT_SPAN = UINT64_SPAN
SEED_TYPE_BITS: int
SEED_BIT_MASK: int
SEED_SIZE: int
STATE_TYPE = SEED_TYPE
ALGORITHM_TYPE = STATE_TYPE
PHILOX_STATE_SIZE: int
THREEFRY_STATE_SIZE: int

class Algorithm(enum.Enum):
    PHILOX: int = ...
    THREEFRY: int = ...

RNG_ALG_PHILOX: Any
RNG_ALG_THREEFRY: Any
DEFAULT_ALGORITHM = RNG_ALG_PHILOX

def non_deterministic_ints(shape: Any, dtype: Any = ...): ...
def create_rng_state(seed: Any, alg: Any): ...

class GeneratorSpec(type_spec.TypeSpec):
    shape: Any = ...
    dtype: Any = ...
    def __init__(self, shape: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    @property
    def value_type(self): ...

class Generator(tracking.AutoTrackable, composite_tensor.CompositeTensor):
    def __init__(self, copy_from: Optional[Any] = ..., state: Optional[Any] = ..., alg: Optional[Any] = ...) -> None: ...
    @classmethod
    def from_state(cls, state: Any, alg: Any): ...
    @classmethod
    def from_seed(cls, seed: Any, alg: Optional[Any] = ...): ...
    @classmethod
    def from_non_deterministic_state(cls, alg: Optional[Any] = ...): ...
    @classmethod
    def from_key_counter(cls, key: Any, counter: Any, alg: Any): ...
    def reset(self, state: Any) -> None: ...
    def reset_from_seed(self, seed: Any) -> None: ...
    def reset_from_key_counter(self, key: Any, counter: Any) -> None: ...
    @property
    def state(self): ...
    @property
    def algorithm(self): ...
    @property
    def key(self): ...
    def skip(self, delta: Any) -> None: ...
    def normal(self, shape: Any, mean: float = ..., stddev: float = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
    def truncated_normal(self, shape: Any, mean: float = ..., stddev: float = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
    def uniform(self, shape: Any, minval: int = ..., maxval: Optional[Any] = ..., dtype: Any = ..., name: Optional[Any] = ...): ...
    def uniform_full_int(self, shape: Any, dtype: Any = ..., name: Optional[Any] = ...): ...
    def binomial(self, shape: Any, counts: Any, probs: Any, dtype: Any = ..., name: Optional[Any] = ...): ...
    def make_seeds(self, count: int = ...): ...
    def split(self, count: int = ...): ...

global_generator: Any

def get_global_generator(): ...
def set_global_generator(generator: Any) -> None: ...