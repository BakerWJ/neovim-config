from tensorflow.python._pywrap_tf_session import *
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from typing import Any, Optional

__git_version__: Any
__compiler_version__: Any
__cxx11_abi_flag__: Any
__monolithic_build__: Any
GRAPH_DEF_VERSION: Any
GRAPH_DEF_VERSION_MIN_CONSUMER: Any
GRAPH_DEF_VERSION_MIN_PRODUCER: Any
TENSOR_HANDLE_KEY: Any

def TF_NewSessionOptions(target: Optional[Any] = ..., config: Optional[Any] = ...): ...
def TF_Reset(target: Any, containers: Optional[Any] = ..., config: Optional[Any] = ...) -> None: ...
