from tensorflow.python.debug.cli import cli_shared as cli_shared, command_parser as command_parser, debugger_cli_common as debugger_cli_common, ui_factory as ui_factory
from tensorflow.python.debug.lib import profiling as profiling, source_utils as source_utils
from typing import Any, Optional

RL: Any
SORT_OPS_BY_OP_NAME: str
SORT_OPS_BY_OP_TYPE: str
SORT_OPS_BY_OP_TIME: str
SORT_OPS_BY_EXEC_TIME: str
SORT_OPS_BY_START_TIME: str
SORT_OPS_BY_LINE: str

class ProfileDataTableView:
    formatted_start_time: Any = ...
    formatted_op_time: Any = ...
    formatted_exec_time: Any = ...
    def __init__(self, profile_datum_list: Any, time_unit: Any = ...) -> None: ...
    def value(self, row: Any, col: Any, device_name_filter: Optional[Any] = ..., node_name_filter: Optional[Any] = ..., op_type_filter: Optional[Any] = ...): ...
    def row_count(self): ...
    def column_count(self): ...
    def column_names(self): ...
    def column_sort_id(self, col: Any): ...

class ProfileAnalyzer:
    def __init__(self, graph: Any, run_metadata: Any) -> None: ...
    def list_profile(self, args: Any, screen_info: Optional[Any] = ...): ...
    def print_source(self, args: Any, screen_info: Optional[Any] = ...): ...
    def get_help(self, handler_name: Any): ...

def create_profiler_ui(graph: Any, run_metadata: Any, ui_type: str = ..., on_ui_exit: Optional[Any] = ..., config: Optional[Any] = ...): ...
