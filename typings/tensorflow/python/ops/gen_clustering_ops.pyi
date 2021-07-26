from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

def kmc2_chain_initialization(distances: Any, seed: Any, name: Optional[Any] = ...): ...

KMC2ChainInitialization: Any

def kmc2_chain_initialization_eager_fallback(distances: Any, seed: Any, name: Any, ctx: Any): ...
def kmeans_plus_plus_initialization(points: Any, num_to_sample: Any, seed: Any, num_retries_per_sample: Any, name: Optional[Any] = ...): ...

KmeansPlusPlusInitialization: Any

def kmeans_plus_plus_initialization_eager_fallback(points: Any, num_to_sample: Any, seed: Any, num_retries_per_sample: Any, name: Any, ctx: Any): ...

_NearestNeighborsOutput = namedtuple('NearestNeighbors', ['nearest_center_indices', 'nearest_center_distances'])

def nearest_neighbors(points: Any, centers: Any, k: Any, name: Optional[Any] = ...): ...

NearestNeighbors: Any

def nearest_neighbors_eager_fallback(points: Any, centers: Any, k: Any, name: Any, ctx: Any): ...
