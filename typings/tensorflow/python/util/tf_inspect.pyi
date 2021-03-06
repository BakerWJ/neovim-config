import inspect as _inspect
from collections import namedtuple
from tensorflow.python.util import tf_decorator as tf_decorator
from typing import Any, Optional

ArgSpec = _inspect.ArgSpec
FullArgSpec = _inspect.FullArgSpec

FullArgSpec = namedtuple('FullArgSpec', ['args', 'varargs', 'varkw', 'defaults', 'kwonlyargs', 'kwonlydefaults', 'annotations'])

def currentframe(): ...
def getargspec(obj: Any): ...
def getfullargspec(obj: Any): ...
def getcallargs(*func_and_positional: Any, **named: Any): ...
def getframeinfo(*args: Any, **kwargs: Any): ...
def getdoc(object: Any): ...
def getfile(object: Any): ...
def getmembers(object: Any, predicate: Optional[Any] = ...): ...
def getmodule(object: Any): ...
def getmro(cls): ...
def getsource(object: Any): ...
def getsourcefile(object: Any): ...
def getsourcelines(object: Any): ...
def isbuiltin(object: Any): ...
def isclass(object: Any): ...
def isfunction(object: Any): ...
def isframe(object: Any): ...
def isgenerator(object: Any): ...
def isgeneratorfunction(object: Any): ...
def ismethod(object: Any): ...
def ismodule(object: Any): ...
def isroutine(object: Any): ...
def stack(context: int = ...): ...
