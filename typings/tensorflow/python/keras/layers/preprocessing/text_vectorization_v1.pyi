from tensorflow.python.keras.engine import base_preprocessing_layer_v1 as base_preprocessing_layer_v1
from tensorflow.python.keras.layers.preprocessing import categorical_encoding_v1 as categorical_encoding_v1, index_lookup_v1 as index_lookup_v1, text_vectorization as text_vectorization
from tensorflow.python.ops.ragged import ragged_tensor_value as ragged_tensor_value
from tensorflow.python.util.tf_export import keras_export as keras_export

class TextVectorization(text_vectorization.TextVectorization, base_preprocessing_layer_v1.CombinerPreprocessingLayer): ...
