def AddStep(arg0: int, arg1: str, arg2: str, arg3: str) -> float: ...
def DeleteProfiler() -> None: ...
def NewProfiler(arg0: str, arg1: str) -> bool: ...
def PrintModelAnalysis(arg0: str, arg1: str, arg2: str, arg3: str, arg4: str) -> bytes: ...
def Profile(arg0: str, arg1: str) -> bytes: ...
def ProfilerFromFile(arg0: str) -> None: ...
def SerializeToString() -> bytes: ...
def WriteProfile(arg0: str) -> None: ...