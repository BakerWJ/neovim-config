from tensorflow.python.util import tf_inspect as tf_inspect
from typing import Any, Optional

SPECIAL_BUILTINS: Any

def islambda(f: Any): ...
def isnamedtuple(f: Any): ...
def isbuiltin(f: Any): ...
def isconstructor(cls): ...
def getimmediatesource(obj: Any): ...
def getnamespace(f: Any): ...
def getqualifiedname(namespace: Any, object_: Any, max_depth: int = ..., visited: Optional[Any] = ...): ...
def getdefiningclass(m: Any, owner_class: Any): ...
def getmethodclass(m: Any): ...
def getfutureimports(entity: Any): ...
