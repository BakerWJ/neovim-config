from tensorflow.python.keras.saving.saved_model import layer_serialization as layer_serialization

class NetworkSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    @property
    def object_identifier(self): ...
