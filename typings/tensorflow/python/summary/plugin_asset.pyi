import abc
from tensorflow.python.framework import ops as ops
from typing import Any, Optional

def get_plugin_asset(plugin_asset_cls: Any, graph: Optional[Any] = ...): ...
def get_all_plugin_assets(graph: Optional[Any] = ...): ...

class PluginAsset(metaclass=abc.ABCMeta):
    plugin_name: Any = ...
    @abc.abstractmethod
    def assets(self) -> Any: ...
