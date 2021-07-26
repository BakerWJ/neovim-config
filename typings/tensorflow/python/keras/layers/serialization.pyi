from tensorflow.python.keras.layers.advanced_activations import *
from tensorflow.python.keras.layers.convolutional import *
from tensorflow.python.keras.layers.convolutional_recurrent import *
from tensorflow.python.keras.layers.core import *
from tensorflow.python.keras.layers.cudnn_recurrent import *
from tensorflow.python.keras.layers.dense_attention import *
from tensorflow.python.keras.layers.embeddings import *
from tensorflow.python.keras.layers.local import *
from tensorflow.python.keras.layers.merge import *
from tensorflow.python.keras.layers.noise import *
from tensorflow.python.keras.layers.normalization import *
from tensorflow.python.keras.layers.pooling import *
from tensorflow.python.keras.layers.preprocessing.image_preprocessing import *
from tensorflow.python.keras.layers.preprocessing.normalization_v1 import *
from tensorflow.python.keras.layers.recurrent import *
from tensorflow.python.keras.layers.rnn_cell_wrapper_v2 import *
from tensorflow.python.keras.layers.wrappers import *
from tensorflow.python.keras.layers.normalization_v2 import *
from tensorflow.python.keras.layers.recurrent_v2 import *
from tensorflow.python.keras.layers.preprocessing.normalization import *
from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.engine.base_layer import AddLoss as AddLoss, AddMetric as AddMetric, TensorFlowOpLayer as TensorFlowOpLayer
from tensorflow.python.keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

def serialize(layer: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
