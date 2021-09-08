from tensorflow.python.eager import backprop_util as backprop_util
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_util as control_flow_util, control_flow_util_v2 as util, custom_gradient as custom_gradient, default_gradient as default_gradient, gen_dataset_ops as gen_dataset_ops, gen_functional_ops as gen_functional_ops, gradients_util as gradients_util, math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any

def cond_v2(pred: Any, true_fn: Any, false_fn: Any, name: str = ...): ...
def get_func_graphs(op: Any): ...
def verify_captures(op_type: Any, branch_graphs: Any) -> None: ...

class _CondGradFuncGraph(util.CondBranchFuncGraph):
    op_needs_rewrite: bool = ...
    def __init__(self, name: Any, forward_graph: Any) -> None: ...
    @property
    def wrapped_intermediates(self): ...
    @property
    def xla_intermediates(self): ...

def indexed_case(branch_index: Any, branch_fns: Any, name: str = ...): ...