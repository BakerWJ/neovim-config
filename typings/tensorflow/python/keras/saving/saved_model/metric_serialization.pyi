from tensorflow.python.keras.saving.saved_model import layer_serialization as layer_serialization
from tensorflow.python.training.tracking import data_structures as data_structures

class MetricSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    @property
    def object_identifier(self): ...
