from typing import Any

class TraceMe:
    def __init__(self, arg0: str) -> None: ...
    def Enter(self) -> None: ...
    def Exit(self) -> None: ...
    def IsEnabled(self, *args, **kwargs) -> Any: ...
