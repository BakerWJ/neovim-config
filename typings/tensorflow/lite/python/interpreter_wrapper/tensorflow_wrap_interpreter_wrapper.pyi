from typing import Any

def swig_import_helper(): ...

class _object: ...

def PyListToStdVectorString(list: Any, strings: Any): ...

PyListToStdVectorString: Any

class InterpreterWrapper(_object):
    __swig_setmethods__: Any = ...
    __setattr__: Any = ...
    __swig_getmethods__: Any = ...
    __getattr__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __swig_destroy__: Any = ...
    __del__: Any = ...
    def AllocateTensors(self): ...
    def Invoke(self): ...
    def InputIndices(self): ...
    def OutputIndices(self): ...
    def ResizeInputTensor(self, i: Any, value: Any): ...
    def NumTensors(self): ...
    def TensorName(self, i: Any): ...
    def TensorType(self, i: Any): ...
    def TensorSize(self, i: Any): ...
    def TensorSizeSignature(self, i: Any): ...
    def TensorSparsityParameters(self, i: Any): ...
    def TensorQuantization(self, i: Any): ...
    def TensorQuantizationParameters(self, i: Any): ...
    def SetTensor(self, i: Any, value: Any): ...
    def GetTensor(self, i: Any): ...
    def ResetVariableTensors(self): ...
    def NumNodes(self): ...
    def NodeName(self, i: Any): ...
    def NodeInputs(self, i: Any): ...
    def NodeOutputs(self, i: Any): ...
    def tensor(self, base_object: Any, i: Any): ...
    def ModifyGraphWithDelegate(self, delegate: Any): ...
    CreateWrapperCPPFromFile: Any = ...
    CreateWrapperCPPFromBuffer: Any = ...

InterpreterWrapper_swigregister: Any

def InterpreterWrapper_CreateWrapperCPPFromFile(*args: Any): ...

InterpreterWrapper_CreateWrapperCPPFromFile: Any

def InterpreterWrapper_CreateWrapperCPPFromBuffer(*args: Any): ...

InterpreterWrapper_CreateWrapperCPPFromBuffer: Any
