from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import context as context
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def to_dlpack(tf_tensor: Any): ...
def from_dlpack(dlcapsule: Any): ...
