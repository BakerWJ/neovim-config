def AssertSameStructure(arg0: handle, arg1: handle, arg2: bool, arg3: bool) -> bool: ...
def AssertSameStructureForData(arg0: handle, arg1: handle, arg2: bool) -> bool: ...
def Flatten(arg0: handle, arg1: bool) -> object: ...
def FlattenForData(arg0: handle) -> object: ...
def IsAttrs(arg0: handle) -> bool: ...
def IsCompositeTensor(arg0: handle) -> bool: ...
def IsMapping(arg0: handle) -> bool: ...
def IsMappingView(arg0: handle) -> bool: ...
def IsMutableMapping(arg0: handle) -> bool: ...
def IsNamedtuple(arg0: handle, arg1: bool) -> object: ...
def IsResourceVariable(arg0: handle) -> bool: ...
def IsSequence(arg0: handle) -> bool: ...
def IsSequenceForData(arg0: handle) -> bool: ...
def IsSequenceOrComposite(arg0: handle) -> bool: ...
def IsTensor(arg0: handle) -> bool: ...
def IsTypeSpec(arg0: handle) -> bool: ...
def IsVariable(arg0: handle) -> bool: ...
def RegisterType(arg0: handle, arg1: handle) -> object: ...
def SameNamedtuples(arg0: handle, arg1: handle) -> object: ...
