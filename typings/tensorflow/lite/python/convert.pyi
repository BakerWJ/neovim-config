import enum
from tensorflow.lite.python import lite_constants as lite_constants, util as util, wrap_toco as wrap_toco
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.util import deprecation as deprecation
from typing import Any, Optional

class OpsSet(enum.Enum):
    TFLITE_BUILTINS: str = ...
    SELECT_TF_OPS: str = ...
    TFLITE_BUILTINS_INT8: str = ...
    @staticmethod
    def get_options(): ...

class ConverterError(Exception): ...

def toco_convert_protos(model_flags_str: Any, toco_flags_str: Any, input_data_str: Any, debug_info_str: Optional[Any] = ..., enable_mlir_converter: bool = ...): ...
def build_toco_convert_protos(input_tensors: Any, output_tensors: Any, inference_type: Any = ..., inference_input_type: Optional[Any] = ..., input_format: Any = ..., input_shapes: Optional[Any] = ..., output_format: Any = ..., quantized_input_stats: Optional[Any] = ..., default_ranges_stats: Optional[Any] = ..., drop_control_dependency: bool = ..., reorder_across_fake_quant: bool = ..., allow_custom_ops: bool = ..., custom_opdefs: Optional[Any] = ..., change_concat_input_ranges: bool = ..., post_training_quantize: bool = ..., quantize_to_float16: bool = ..., dump_graphviz_dir: Optional[Any] = ..., dump_graphviz_video: bool = ..., target_ops: Optional[Any] = ..., allow_nonexistent_arrays: bool = ..., debug_info: Optional[Any] = ..., conversion_summary_dir: Optional[Any] = ...): ...
def toco_convert_graph_def(input_data: Any, input_arrays_with_shape: Any, output_arrays: Any, enable_mlir_converter: Any, *args: Any, **kwargs: Any): ...
def toco_convert_impl(input_data: Any, input_tensors: Any, output_tensors: Any, enable_mlir_converter: Any, *args: Any, **kwargs: Any): ...
def toco_convert(input_data: Any, input_tensors: Any, output_tensors: Any, *args: Any, **kwargs: Any): ...
