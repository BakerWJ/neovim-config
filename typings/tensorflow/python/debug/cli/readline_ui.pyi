from tensorflow.python.debug.cli import base_ui as base_ui, debugger_cli_common as debugger_cli_common
from typing import Any, Optional

class ReadlineUI(base_ui.BaseUI):
    def __init__(self, on_ui_exit: Optional[Any] = ..., config: Optional[Any] = ...) -> None: ...
    def run_ui(self, init_command: Optional[Any] = ..., title: Optional[Any] = ..., title_color: Optional[Any] = ..., enable_mouse_on_start: bool = ...): ...
