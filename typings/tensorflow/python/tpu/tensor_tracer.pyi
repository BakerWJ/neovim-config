from tensorflow.core.framework import summary_pb2 as summary_pb2
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, graph_io as graph_io, ops as ops, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, gen_math_ops as gen_math_ops, init_ops as init_ops, linalg_ops as linalg_ops, logging_ops as logging_ops, math_ops as math_ops, nn_impl as nn_impl, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.platform import analytics as analytics, gfile as gfile
from tensorflow.python.summary import summary_iterator as summary_iterator
from tensorflow.python.tpu import tensor_tracer_flags as tensor_tracer_flags, tensor_tracer_report as tensor_tracer_report, tpu as tpu
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.training import training_util as training_util
from typing import Any, Optional

def op_priority(op_type: Any): ...
def read_tensor_tracer_event_file(event_file: Any): ...
def tensor_tracepoint(tensor: Any, checkpoint_name: Any): ...
def keras_layer_tracepoint(layer: Any, checkpoint_name: Any): ...

class TensorTracer:
    @staticmethod
    def is_enabled(): ...
    @staticmethod
    def check_device_type(device_type: Any) -> None: ...
    @staticmethod
    def check_trace_mode(device_type: Any, trace_mode: Any) -> None: ...
    @staticmethod
    def loop_cond_op(op: Any): ...
    @staticmethod
    def while_loop_op(op: Any): ...
    @staticmethod
    def control_flow_op(op: Any): ...
    @staticmethod
    def unsafe_op(op: Any): ...
    @staticmethod
    def device_mismatch(device_type: Any, op: Any): ...
    @staticmethod
    def unsafe_scalar_trace(op: Any): ...
    @staticmethod
    def reason(op_idx: Any, details: Any): ...
    def __init__(self) -> None: ...
    def host_call_deps_and_fn(self): ...
    def get_traced_op_names(self): ...
    def trace_tpu(self, graph: Any, tensor_fetches: Any, op_fetches: Optional[Any] = ..., num_replicas: Optional[Any] = ..., num_replicas_per_host: Optional[Any] = ..., num_hosts: Optional[Any] = ...): ...
    def trace_cpu(self, graph: Any, tensor_fetches: Any, op_fetches: Optional[Any] = ...): ...
