from typing import Any

class TraceMe:
    def __init__(self, name: Any, **kwargs: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

def traceme_wrapper(func: Any): ...
