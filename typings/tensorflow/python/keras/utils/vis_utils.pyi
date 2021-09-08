from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def check_pydot(): ...
def is_wrapped_model(layer: Any): ...
def add_edge(dot: Any, src: Any, dst: Any) -> None: ...
def model_to_dot(model: Any, show_shapes: bool = ..., show_layer_names: bool = ..., rankdir: str = ..., expand_nested: bool = ..., dpi: int = ..., subgraph: bool = ...): ...
def plot_model(model: Any, to_file: str = ..., show_shapes: bool = ..., show_layer_names: bool = ..., rankdir: str = ..., expand_nested: bool = ..., dpi: int = ...): ...