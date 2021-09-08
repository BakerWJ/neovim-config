from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.lib.io import file_io as file_io
from typing import Any, Optional

def write_dirpath(dirpath: Any, strategy: Optional[Any] = ...): ...
def remove_temp_dirpath(dirpath: Any, strategy: Optional[Any] = ...) -> None: ...