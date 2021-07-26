from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.engine.training import Model as Model
from tensorflow.python.keras.layers.core import Lambda as Lambda
from tensorflow.python.keras.layers.merge import concatenate as concatenate
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def multi_gpu_model(model: Any, gpus: Any, cpu_merge: bool = ..., cpu_relocation: bool = ...): ...
