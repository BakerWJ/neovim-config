class ProfilerSession:
    def __init__(self) -> None: ...
    def export_to_tb(self) -> None: ...
    def start(self, arg0: str) -> None: ...
    def stop(self) -> bytes: ...

def monitor(arg0: str, arg1: int, arg2: int, arg3: bool) -> str: ...
def start_server(arg0: int) -> None: ...
def trace(arg0: str, arg1: str, arg2: str, arg3: bool, arg4: int, arg5: int) -> None: ...