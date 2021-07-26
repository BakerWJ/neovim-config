from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.engine import base_preprocessing_layer as base_preprocessing_layer, sequential as sequential
from tensorflow.python.keras.utils import tf_utils as tf_utils
from typing import Any

class PreprocessingStage(base_preprocessing_layer.PreprocessingLayer, sequential.Sequential):
    def adapt(self, data: Any, reset_state: bool = ...): ...
