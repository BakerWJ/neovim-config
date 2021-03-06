from typing import Any, Optional

class Client:
    def __init__(self, tpu: Optional[Any] = ..., zone: Optional[Any] = ..., project: Optional[Any] = ..., credentials: str = ..., service: Optional[Any] = ..., discovery_url: Optional[Any] = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def recoverable(self): ...
    def state(self): ...
    def health(self): ...
    def runtime_version(self): ...
    def accelerator_type(self): ...
    def api_available(self): ...
    def name(self): ...
    def get_local_ip(self): ...
    def network_endpoints(self): ...
    def wait_for_healthy(self, timeout_s: int = ..., interval: int = ...) -> None: ...
    def configure_tpu_version(self, version: Any) -> None: ...
