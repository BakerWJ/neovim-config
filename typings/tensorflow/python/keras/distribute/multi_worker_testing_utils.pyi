from tensorflow.python import keras as keras
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras.optimizer_v2 import gradient_descent as gradient_descent
from tensorflow.python.ops import array_ops as array_ops, random_ops as random_ops
from typing import Any

def mnist_synthetic_dataset(batch_size: Any, steps_per_epoch: Any): ...
def get_mnist_model(input_shape: Any): ...
