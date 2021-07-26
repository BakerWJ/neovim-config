from keras_preprocessing import sequence
from tensorflow.python.keras.utils import data_utils as data_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any, Optional

make_sampling_table: Any
skipgrams: Any

class TimeseriesGenerator(sequence.TimeseriesGenerator, data_utils.Sequence): ...

def pad_sequences(sequences: Any, maxlen: Optional[Any] = ..., dtype: str = ..., padding: str = ..., truncating: str = ..., value: float = ...): ...
