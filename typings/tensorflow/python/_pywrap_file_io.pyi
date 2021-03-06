from typing import List

class BufferedInputStream:
    def __init__(self, arg0: str, arg1: int) -> None: ...
    def read(self, arg0: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def seek(self, arg0: int) -> None: ...
    def tell(self) -> int: ...

class FileStatistics:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def is_directory(self) -> bool: ...
    @property
    def length(self) -> int: ...
    @property
    def mtime_nsec(self) -> int: ...

class WritableFile:
    def __init__(self, arg0: str, arg1: str) -> None: ...
    def append(self, arg0: str) -> None: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def tell(self) -> int: ...

def CopyFile(arg0: str, arg1: str, arg2: bool) -> None: ...
def CreateDir(arg0: str) -> None: ...
def DeleteFile(arg0: str) -> None: ...
def DeleteRecursively(arg0: str) -> None: ...
def FileExists(arg0: str) -> None: ...
def GetChildren(arg0: str) -> List[str]: ...
def GetMatchingFiles(arg0: str) -> List[str]: ...
def HasAtomicMove(arg0: str) -> bool: ...
def IsDirectory(arg0: str) -> bool: ...
def ReadFileToString(arg0: str) -> bytes: ...
def RecursivelyCreateDir(arg0: str) -> None: ...
def RenameFile(arg0: str, arg1: str, arg2: bool) -> None: ...
def Stat(arg0: str) -> FileStatistics: ...
def WriteStringToFile(arg0: str, arg1: str) -> Status: ...
