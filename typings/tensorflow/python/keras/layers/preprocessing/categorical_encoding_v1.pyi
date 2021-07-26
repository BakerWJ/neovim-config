from tensorflow.python.keras.engine import base_preprocessing_layer_v1 as base_preprocessing_layer_v1
from tensorflow.python.keras.layers.preprocessing import categorical_encoding as categorical_encoding

class CategoricalEncoding(categorical_encoding.CategoricalEncoding, base_preprocessing_layer_v1.CombinerPreprocessingLayer): ...
