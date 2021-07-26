from tensorflow.python.keras.engine import base_preprocessing_layer_v1 as base_preprocessing_layer_v1
from tensorflow.python.keras.layers.preprocessing import index_lookup as index_lookup
from tensorflow.python.ops.ragged import ragged_tensor_value as ragged_tensor_value

class IndexLookup(index_lookup.IndexLookup, base_preprocessing_layer_v1.CombinerPreprocessingLayer):
    def vocab_size(self): ...
