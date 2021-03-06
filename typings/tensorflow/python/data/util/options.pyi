from typing import Any

class OptionsBase:
    def __init__(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __setattr__(self, name: Any, value: Any) -> None: ...

def create_option(name: Any, ty: Any, docstring: Any, default_factory: Any = ...): ...
def merge_options(*options_list: Any): ...
