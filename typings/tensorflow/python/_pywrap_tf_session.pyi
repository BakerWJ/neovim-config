from typing import Any, ClassVar, List, Optional

from typing import overload
import tensorflow.python._pywrap_tfe
TF_ABORTED: TF_Code
TF_BFLOAT16: TF_DataType
TF_BOOL: TF_DataType
TF_CANCELLED: TF_Code
TF_COMPLEX: TF_DataType
TF_COMPLEX128: TF_DataType
TF_COMPLEX64: TF_DataType
TF_DATA_LOSS: TF_Code
TF_DEADLINE_EXCEEDED: TF_Code
TF_DOUBLE: TF_DataType
TF_FAILED_PRECONDITION: TF_Code
TF_FLOAT: TF_DataType
TF_HALF: TF_DataType
TF_INT16: TF_DataType
TF_INT32: TF_DataType
TF_INT64: TF_DataType
TF_INT8: TF_DataType
TF_INTERNAL: TF_Code
TF_INVALID_ARGUMENT: TF_Code
TF_OK: TF_Code
TF_OUT_OF_RANGE: TF_Code
TF_PERMISSION_DENIED: TF_Code
TF_QINT16: TF_DataType
TF_QINT32: TF_DataType
TF_QINT8: TF_DataType
TF_QUINT16: TF_DataType
TF_QUINT8: TF_DataType
TF_RESOURCE: TF_DataType
TF_RESOURCE_EXHAUSTED: TF_Code
TF_STRING: TF_DataType
TF_UINT16: TF_DataType
TF_UINT32: TF_DataType
TF_UINT64: TF_DataType
TF_UINT8: TF_DataType
TF_UNAUTHENTICATED: TF_Code
TF_UNIMPLEMENTED: TF_Code
TF_UNKNOWN: TF_Code
TF_VARIANT: TF_DataType

class TF_ApiDefMap:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Buffer:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Code:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    TF_ABORTED: ClassVar[TF_Code] = ...
    TF_CANCELLED: ClassVar[TF_Code] = ...
    TF_DATA_LOSS: ClassVar[TF_Code] = ...
    TF_DEADLINE_EXCEEDED: ClassVar[TF_Code] = ...
    TF_FAILED_PRECONDITION: ClassVar[TF_Code] = ...
    TF_INTERNAL: ClassVar[TF_Code] = ...
    TF_INVALID_ARGUMENT: ClassVar[TF_Code] = ...
    TF_OK: ClassVar[TF_Code] = ...
    TF_OUT_OF_RANGE: ClassVar[TF_Code] = ...
    TF_PERMISSION_DENIED: ClassVar[TF_Code] = ...
    TF_RESOURCE_EXHAUSTED: ClassVar[TF_Code] = ...
    TF_UNAUTHENTICATED: ClassVar[TF_Code] = ...
    TF_UNIMPLEMENTED: ClassVar[TF_Code] = ...
    TF_UNKNOWN: ClassVar[TF_Code] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __ne__(self, other) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def name(self) -> str: ...

class TF_DataType:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    TF_BFLOAT16: ClassVar[TF_DataType] = ...
    TF_BOOL: ClassVar[TF_DataType] = ...
    TF_COMPLEX: ClassVar[TF_DataType] = ...
    TF_COMPLEX128: ClassVar[TF_DataType] = ...
    TF_COMPLEX64: ClassVar[TF_DataType] = ...
    TF_DOUBLE: ClassVar[TF_DataType] = ...
    TF_FLOAT: ClassVar[TF_DataType] = ...
    TF_HALF: ClassVar[TF_DataType] = ...
    TF_INT16: ClassVar[TF_DataType] = ...
    TF_INT32: ClassVar[TF_DataType] = ...
    TF_INT64: ClassVar[TF_DataType] = ...
    TF_INT8: ClassVar[TF_DataType] = ...
    TF_QINT16: ClassVar[TF_DataType] = ...
    TF_QINT32: ClassVar[TF_DataType] = ...
    TF_QINT8: ClassVar[TF_DataType] = ...
    TF_QUINT16: ClassVar[TF_DataType] = ...
    TF_QUINT8: ClassVar[TF_DataType] = ...
    TF_RESOURCE: ClassVar[TF_DataType] = ...
    TF_STRING: ClassVar[TF_DataType] = ...
    TF_UINT16: ClassVar[TF_DataType] = ...
    TF_UINT32: ClassVar[TF_DataType] = ...
    TF_UINT64: ClassVar[TF_DataType] = ...
    TF_UINT8: ClassVar[TF_DataType] = ...
    TF_VARIANT: ClassVar[TF_DataType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __ne__(self, other) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def name(self) -> str: ...

class TF_DeprecatedSession:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Graph:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_ImportGraphDefOptions:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_ImportGraphDefResults:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Input:
    index: int
    oper: TF_Operation
    def __init__(self) -> None: ...

class TF_Library:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Operation:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_OperationDescription:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Output:
    index: int
    oper: TF_Operation
    def __init__(self) -> None: ...

class TF_Server:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Session:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_SessionOptions:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Status:
    def __init__(self, *args, **kwargs) -> None: ...

def AddControlInput(arg0: TF_Graph, arg1: TF_Operation, arg2: TF_Operation) -> None: ...
def AddWhileInputHack(arg0: TF_Graph, arg1: TF_Output, arg2: TF_Operation) -> None: ...
def ClearAttr(arg0: TF_Graph, arg1: TF_Operation, arg2: str) -> None: ...
@overload
def EqualAttrValueWrapper(arg0: str, arg1: str) -> str: ...
@overload
def EqualAttrValueWrapper(arg0: str, arg1: str) -> str: ...
def EqualGraphDefWrapper(arg0: str, arg1: str) -> str: ...
def ExtendSession(arg0: TF_Session) -> None: ...
def GetHandleShapeAndType(arg0: TF_Graph, arg1: TF_Output) -> bytes: ...
def GetOperationInputs(arg0: TF_Operation) -> List[TF_Output]: ...
def RemoveAllControlInputs(arg0: TF_Graph, arg1: TF_Operation) -> None: ...
def SetAttr(arg0: TF_Graph, arg1: TF_Operation, arg2: str, arg3: TF_Buffer) -> None: ...
def SetHandleShapeAndType(arg0: TF_Graph, arg1: TF_Output, arg2: str) -> None: ...
def SetRequestedDevice(arg0: TF_Graph, arg1: TF_Operation, arg2: str) -> None: ...
def SetRequireShapeInferenceFns(arg0: TF_Graph, arg1: bool) -> None: ...
def TF_AddControlInput(arg0: TF_OperationDescription, arg1: TF_Operation) -> None: ...
def TF_AddInput(arg0: TF_OperationDescription, arg1: TF_Output) -> None: ...
def TF_AddInputList(arg0: TF_OperationDescription, arg1: handle) -> None: ...
def TF_ApiDefMapGet(arg0: TF_ApiDefMap, arg1: str, arg2: int) -> TF_Buffer: ...
def TF_ApiDefMapPut(arg0: TF_ApiDefMap, arg1: str, arg2: int) -> None: ...
def TF_CloseSession(arg0: TF_Session) -> None: ...
def TF_CreatePlaceholders(arg0: TF_Graph, arg1: handle, arg2: str) -> List[TF_Output]: ...
def TF_DeleteApiDefMap(arg0: TF_ApiDefMap) -> None: ...
def TF_DeleteBuffer(arg0: TF_Buffer) -> None: ...
@overload
def TF_DeleteDeviceList(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList) -> None: ...
@overload
def TF_DeleteDeviceList(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList) -> None: ...
def TF_DeleteFunction(arg0: tensorflow.python._pywrap_tfe.TF_Function) -> None: ...
def TF_DeleteGraph(arg0: TF_Graph) -> None: ...
def TF_DeleteImportGraphDefOptions(arg0: TF_ImportGraphDefOptions) -> None: ...
def TF_DeleteImportGraphDefResults(arg0: TF_ImportGraphDefResults) -> None: ...
def TF_DeleteLibraryHandle(arg0: TF_Library) -> None: ...
def TF_DeleteSession(arg0: TF_Session) -> None: ...
def TF_DeleteSessionOptions(arg0: TF_SessionOptions) -> None: ...
def TF_DeleteStatus(arg0: TF_Status) -> None: ...
def TF_DeviceListCount(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList) -> int: ...
def TF_DeviceListIncarnation(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList, arg1: int) -> int: ...
def TF_DeviceListMemoryBytes(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList, arg1: int) -> int: ...
def TF_DeviceListName(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList, arg1: int) -> str: ...
def TF_DeviceListType(arg0: tensorflow.python._pywrap_tfe.TF_DeviceList, arg1: int) -> str: ...
def TF_FinishOperation(arg0: TF_OperationDescription) -> TF_Operation: ...
def TF_FunctionImportFunctionDef(arg0: str) -> tensorflow.python._pywrap_tfe.TF_Function: ...
def TF_FunctionSetAttrValueProto(arg0: tensorflow.python._pywrap_tfe.TF_Function, arg1: str, arg2: str) -> None: ...
def TF_FunctionToFunctionDef(arg0: tensorflow.python._pywrap_tfe.TF_Function, arg1: TF_Buffer) -> None: ...
def TF_GetAllOpList() -> TF_Buffer: ...
def TF_GetAllRegisteredKernels() -> TF_Buffer: ...
def TF_GetBuffer(arg0: TF_Buffer) -> object: ...
def TF_GetCode(arg0: TF_Status) -> TF_Code: ...
def TF_GetOpList(arg0: TF_Library) -> object: ...
def TF_GetRegisteredKernelsForOp(arg0: str) -> TF_Buffer: ...
def TF_GetXlaConstantFoldingDisabled() -> int: ...
def TF_GraphCopyFunction(arg0: TF_Graph, arg1: tensorflow.python._pywrap_tfe.TF_Function, arg2: tensorflow.python._pywrap_tfe.TF_Function) -> None: ...
def TF_GraphGetOpDef(arg0: TF_Graph, arg1: str, arg2: TF_Buffer) -> None: ...
def TF_GraphGetTensorShapeHelper(arg0: TF_Graph, arg1: TF_Output) -> tuple: ...
def TF_GraphGetTensorShape_wrapper(arg0: TF_Graph, arg1: TF_Output, arg2: List[int], arg3: bool) -> None: ...
def TF_GraphImportGraphDefWithResults(arg0: TF_Graph, arg1: TF_Buffer, arg2: TF_ImportGraphDefOptions) -> TF_ImportGraphDefResults: ...
def TF_GraphNextOperation(arg0: TF_Graph, arg1: int) -> tuple: ...
def TF_GraphSetOutputHandleShapesAndTypes_wrapper(arg0: TF_Graph, arg1: TF_Output, arg2: List[Optional[List[int]]], arg3: List[int], arg4: handle) -> None: ...
def TF_GraphSetTensorShape_wrapper(arg0: TF_Graph, arg1: TF_Output, arg2: List[int], arg3: bool) -> None: ...
def TF_GraphToFunction_wrapper(arg0: TF_Graph, arg1: str, arg2: bool, arg3: Optional[List[TF_Operation]], arg4: List[TF_Output], arg5: List[TF_Output], arg6: List[bytes], arg7: List[TF_Operation], arg8: List[bytes], arg9: none, arg10: str) -> tensorflow.python._pywrap_tfe.TF_Function: ...
def TF_GraphToGraphDef(arg0: TF_Graph, arg1: TF_Buffer) -> None: ...
def TF_GraphVersions(arg0: TF_Graph, arg1: TF_Buffer) -> None: ...
def TF_ImportGraphDefOptionsAddInputMapping(arg0: TF_ImportGraphDefOptions, arg1: str, arg2: int, arg3: TF_Output) -> None: ...
def TF_ImportGraphDefOptionsAddReturnOperation(arg0: TF_ImportGraphDefOptions, arg1: str) -> None: ...
def TF_ImportGraphDefOptionsAddReturnOutput(arg0: TF_ImportGraphDefOptions, arg1: str, arg2: int) -> None: ...
def TF_ImportGraphDefOptionsRemapControlDependency(arg0: TF_ImportGraphDefOptions, arg1: str, arg2: TF_Operation) -> None: ...
def TF_ImportGraphDefOptionsSetPrefix(arg0: TF_ImportGraphDefOptions, arg1: str) -> None: ...
def TF_ImportGraphDefOptionsSetUniquifyNames(arg0: TF_ImportGraphDefOptions, arg1: int) -> None: ...
def TF_ImportGraphDefOptionsSetValidateColocationConstraints(arg0: TF_ImportGraphDefOptions, arg1: int) -> None: ...
def TF_ImportGraphDefResultsMissingUnusedInputMappings_wrapper(arg0: TF_ImportGraphDefResults) -> List[str]: ...
def TF_ImportGraphDefResultsReturnOperations(arg0: TF_ImportGraphDefResults) -> list: ...
def TF_ImportGraphDefResultsReturnOutputs(arg0: TF_ImportGraphDefResults) -> list: ...
def TF_LoadLibrary(arg0: str) -> TF_Library: ...
def TF_NewApiDefMap(arg0: TF_Buffer) -> TF_ApiDefMap: ...
def TF_NewBuffer() -> TF_Buffer: ...
def TF_NewBufferFromString(arg0: str) -> TF_Buffer: ...
def TF_NewGraph() -> TF_Graph: ...
def TF_NewImportGraphDefOptions() -> TF_ImportGraphDefOptions: ...
def TF_NewOperation(arg0: TF_Graph, arg1: str, arg2: str) -> TF_OperationDescription: ...
def TF_NewServer(arg0: str) -> TF_Server: ...
def TF_NewSession(arg0: TF_Graph, arg1: TF_SessionOptions) -> TF_Session: ...
def TF_NewSessionRef(arg0: TF_Graph, arg1: TF_SessionOptions) -> TF_Session: ...
def TF_NewStatus() -> TF_Status: ...
def TF_OperationDevice(arg0: TF_Operation) -> str: ...
def TF_OperationGetAttrBool(arg0: TF_Operation, arg1: str) -> object: ...
def TF_OperationGetAttrInt(arg0: TF_Operation, arg1: str) -> object: ...
def TF_OperationGetAttrType(arg0: TF_Operation, arg1: str) -> TF_DataType: ...
def TF_OperationGetAttrValueProto(arg0: TF_Operation, arg1: str, arg2: TF_Buffer) -> None: ...
def TF_OperationGetControlInputs_wrapper(arg0: TF_Operation) -> List[TF_Operation]: ...
def TF_OperationGetControlOutputs_wrapper(arg0: TF_Operation) -> List[TF_Operation]: ...
def TF_OperationInputType(arg0: TF_Input) -> TF_DataType: ...
def TF_OperationName(arg0: TF_Operation) -> str: ...
def TF_OperationNumInputs(arg0: TF_Operation) -> int: ...
def TF_OperationNumOutputs(arg0: TF_Operation) -> int: ...
def TF_OperationOpType(arg0: TF_Operation) -> str: ...
def TF_OperationOutputConsumers_wrapper(arg0: TF_Output) -> List[str]: ...
def TF_OperationOutputType(arg0: TF_Output) -> TF_DataType: ...
def TF_OperationToNodeDef(arg0: TF_Operation, arg1: TF_Buffer) -> None: ...
def TF_Reset_wrapper(arg0: TF_SessionOptions, arg1: List[bytes]) -> None: ...
def TF_ServerJoin(arg0: TF_Server) -> None: ...
def TF_ServerStart(arg0: TF_Server) -> None: ...
def TF_ServerStop(arg0: TF_Server) -> None: ...
def TF_ServerTarget(arg0: TF_Server) -> str: ...
def TF_SessionListDevices(arg0: TF_Session) -> tensorflow.python._pywrap_tfe.TF_DeviceList: ...
def TF_SessionMakeCallable(arg0: TF_Session, arg1: TF_Buffer) -> int: ...
def TF_SessionPRunSetup_wrapper(arg0: TF_Session, arg1: List[TF_Output], arg2: List[TF_Output], arg3: List[TF_Operation]) -> str: ...
def TF_SessionPRun_wrapper(arg0: TF_Session, arg1: str, arg2: handle, arg3: List[TF_Output]) -> object: ...
def TF_SessionReleaseCallable(arg0: TF_Session, arg1: int) -> None: ...
def TF_SessionRunCallable(arg0: TF_Session, arg1: int, arg2: object, arg3: TF_Buffer) -> list: ...
def TF_SessionRun_wrapper(arg0: TF_Session, arg1: TF_Buffer, arg2: handle, arg3: List[TF_Output], arg4: List[TF_Operation], arg5: TF_Buffer) -> object: ...
def TF_SetAttrValueProto(arg0: TF_OperationDescription, arg1: str, arg2: str) -> None: ...
def TF_SetDevice(arg0: TF_OperationDescription, arg1: str) -> None: ...
def TF_SetTfXlaCpuGlobalJit(arg0: int) -> int: ...
@overload
def TF_SetXlaAutoJitMode(arg0: str) -> None: ...
@overload
def TF_SetXlaAutoJitMode(arg0: str) -> None: ...
def TF_SetXlaConstantFoldingDisabled(arg0: int) -> None: ...
def TF_SetXlaEnableLazyCompilation(arg0: int) -> int: ...
def TF_SetXlaMinClusterSize(arg0: int) -> None: ...
def TF_TryEvaluateConstant_wrapper(arg0: TF_Graph, arg1: TF_Output) -> object: ...
def UpdateEdge(arg0: TF_Graph, arg1: TF_Output, arg2: TF_Input) -> None: ...
def _TF_NewSessionOptions() -> TF_SessionOptions: ...
def _TF_SetConfig(arg0: TF_SessionOptions, arg1: str) -> None: ...
def _TF_SetTarget(arg0: TF_SessionOptions, arg1: str) -> None: ...
def get_compiler_version() -> str: ...
def get_cxx11_abi_flag() -> int: ...
def get_git_version() -> str: ...
def get_graph_def_version() -> int: ...
def get_graph_def_version_min_consumer() -> int: ...
def get_graph_def_version_min_producer() -> int: ...
def get_monolithic_build() -> int: ...
def get_tensor_handle_key() -> str: ...
def get_version() -> str: ...
