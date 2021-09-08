from typing import Any

html_escape_table: Any

def html_escape(text: Any): ...
def get_input_type_from_signature(op_signature: Any): ...
def get_operator_type(op_name: Any, conversion_log: Any): ...

class HTMLGenerator:
    html_template: Any = ...
    export_report_path: Any = ...
    def __init__(self, html_template_path: Any, export_report_path: Any) -> None: ...
    def generate(self, toco_conversion_log_before: Any, toco_conversion_log_after: Any, post_training_quant_enabled: Any, dot_before: Any, dot_after: Any, toco_err_log: str = ..., tflite_graph_path: str = ...) -> None: ...

def gen_conversion_log_html(conversion_log_dir: Any, quantization_enabled: Any, tflite_graph_path: Any) -> None: ...