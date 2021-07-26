from tensorflow.python.keras.saving import saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import constants as constants, network_serialization as network_serialization, save_impl as save_impl

class ModelSavedModelSaver(network_serialization.NetworkSavedModelSaver):
    @property
    def object_identifier(self): ...

class SequentialSavedModelSaver(ModelSavedModelSaver):
    @property
    def object_identifier(self): ...
