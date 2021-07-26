from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import signature_constants as signature_constants, signature_def_utils as signature_def_utils, tag_constants as tag_constants
from tensorflow.python.saved_model.model_utils import mode_keys as mode_keys
from tensorflow.python.util import compat as compat
from typing import Any, Optional

EXPORT_TAG_MAP: Any
SIGNATURE_KEY_MAP: Any
SINGLE_FEATURE_DEFAULT_NAME: str
SINGLE_RECEIVER_DEFAULT_NAME: str
SINGLE_LABEL_DEFAULT_NAME: str

def build_all_signature_defs(receiver_tensors: Any, export_outputs: Any, receiver_tensors_alternatives: Optional[Any] = ..., serving_only: bool = ...): ...

MAX_DIRECTORY_CREATION_ATTEMPTS: int

def get_timestamped_export_dir(export_dir_base: Any): ...
def get_temp_export_dir(timestamped_export_dir: Any): ...
def export_outputs_for_mode(mode: Any, serving_export_outputs: Optional[Any] = ..., predictions: Optional[Any] = ..., loss: Optional[Any] = ..., metrics: Optional[Any] = ...): ...
def get_export_outputs(export_outputs: Any, predictions: Any): ...
