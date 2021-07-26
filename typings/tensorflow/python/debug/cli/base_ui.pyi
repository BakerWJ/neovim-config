from tensorflow.python.debug.cli import cli_config as cli_config, command_parser as command_parser, debugger_cli_common as debugger_cli_common
from typing import Any, Optional

class BaseUI:
    CLI_PROMPT: str = ...
    CLI_EXIT_COMMANDS: Any = ...
    ERROR_MESSAGE_PREFIX: str = ...
    INFO_MESSAGE_PREFIX: str = ...
    def __init__(self, on_ui_exit: Optional[Any] = ..., config: Optional[Any] = ...) -> None: ...
    def set_help_intro(self, help_intro: Any) -> None: ...
    def register_command_handler(self, prefix: Any, handler: Any, help_info: Any, prefix_aliases: Optional[Any] = ...) -> None: ...
    def register_tab_comp_context(self, *args: Any, **kwargs: Any) -> None: ...
    def run_ui(self, init_command: Optional[Any] = ..., title: Optional[Any] = ..., title_color: Optional[Any] = ..., enable_mouse_on_start: bool = ...) -> None: ...
    @property
    def config(self): ...
