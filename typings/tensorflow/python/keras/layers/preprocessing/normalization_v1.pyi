from tensorflow.python.keras.engine.base_preprocessing_layer_v1 import CombinerPreprocessingLayer as CombinerPreprocessingLayer
from tensorflow.python.keras.layers.preprocessing import normalization as normalization
from tensorflow.python.util.tf_export import keras_export as keras_export

class Normalization(normalization.Normalization, CombinerPreprocessingLayer): ...
