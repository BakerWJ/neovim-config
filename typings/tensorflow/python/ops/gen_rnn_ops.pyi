from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_BlockLSTMOutput = namedtuple('BlockLSTM', ['i', 'cs', 'f', 'o', 'ci', 'co', 'h'])

def block_lstm(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, forget_bias: int = ..., cell_clip: int = ..., use_peephole: bool = ..., name: Optional[Any] = ...): ...

BlockLSTM: Any

def block_lstm_eager_fallback(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, forget_bias: Any, cell_clip: Any, use_peephole: Any, name: Any, ctx: Any): ...

_BlockLSTMGradOutput = namedtuple('BlockLSTMGrad', ['x_grad', 'cs_prev_grad', 'h_prev_grad', 'w_grad', 'wci_grad', 'wcf_grad', 'wco_grad', 'b_grad'])

def block_lstm_grad(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, i: Any, cs: Any, f: Any, o: Any, ci: Any, co: Any, h: Any, cs_grad: Any, h_grad: Any, use_peephole: Any, name: Optional[Any] = ...): ...

BlockLSTMGrad: Any

def block_lstm_grad_eager_fallback(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, i: Any, cs: Any, f: Any, o: Any, ci: Any, co: Any, h: Any, cs_grad: Any, h_grad: Any, use_peephole: Any, name: Any, ctx: Any): ...

_BlockLSTMGradV2Output = namedtuple('BlockLSTMGradV2', ['x_grad', 'cs_prev_grad', 'h_prev_grad', 'w_grad', 'wci_grad', 'wcf_grad', 'wco_grad', 'b_grad'])

def block_lstm_grad_v2(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, i: Any, cs: Any, f: Any, o: Any, ci: Any, co: Any, h: Any, cs_grad: Any, h_grad: Any, use_peephole: Any, name: Optional[Any] = ...): ...

BlockLSTMGradV2: Any

def block_lstm_grad_v2_eager_fallback(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, i: Any, cs: Any, f: Any, o: Any, ci: Any, co: Any, h: Any, cs_grad: Any, h_grad: Any, use_peephole: Any, name: Any, ctx: Any): ...

_BlockLSTMV2Output = namedtuple('BlockLSTMV2', ['i', 'cs', 'f', 'o', 'ci', 'co', 'h'])

def block_lstmv2(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, cell_clip: int = ..., use_peephole: bool = ..., name: Optional[Any] = ...): ...

BlockLSTMV2: Any

def block_lstmv2_eager_fallback(seq_len_max: Any, x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, cell_clip: Any, use_peephole: Any, name: Any, ctx: Any): ...

_GRUBlockCellOutput = namedtuple('GRUBlockCell', ['r', 'u', 'c', 'h'])

def gru_block_cell(x: Any, h_prev: Any, w_ru: Any, w_c: Any, b_ru: Any, b_c: Any, name: Optional[Any] = ...): ...

GRUBlockCell: Any

def gru_block_cell_eager_fallback(x: Any, h_prev: Any, w_ru: Any, w_c: Any, b_ru: Any, b_c: Any, name: Any, ctx: Any): ...

_GRUBlockCellGradOutput = namedtuple('GRUBlockCellGrad', ['d_x', 'd_h_prev', 'd_c_bar', 'd_r_bar_u_bar'])

def gru_block_cell_grad(x: Any, h_prev: Any, w_ru: Any, w_c: Any, b_ru: Any, b_c: Any, r: Any, u: Any, c: Any, d_h: Any, name: Optional[Any] = ...): ...

GRUBlockCellGrad: Any

def gru_block_cell_grad_eager_fallback(x: Any, h_prev: Any, w_ru: Any, w_c: Any, b_ru: Any, b_c: Any, r: Any, u: Any, c: Any, d_h: Any, name: Any, ctx: Any): ...

_LSTMBlockCellOutput = namedtuple('LSTMBlockCell', ['i', 'cs', 'f', 'o', 'ci', 'co', 'h'])

def lstm_block_cell(x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, forget_bias: int = ..., cell_clip: int = ..., use_peephole: bool = ..., name: Optional[Any] = ...): ...

LSTMBlockCell: Any

def lstm_block_cell_eager_fallback(x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, forget_bias: Any, cell_clip: Any, use_peephole: Any, name: Any, ctx: Any): ...

_LSTMBlockCellGradOutput = namedtuple('LSTMBlockCellGrad', ['cs_prev_grad', 'dicfo', 'wci_grad', 'wcf_grad', 'wco_grad'])

def lstm_block_cell_grad(x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, i: Any, cs: Any, f: Any, o: Any, ci: Any, co: Any, cs_grad: Any, h_grad: Any, use_peephole: Any, name: Optional[Any] = ...): ...

LSTMBlockCellGrad: Any

def lstm_block_cell_grad_eager_fallback(x: Any, cs_prev: Any, h_prev: Any, w: Any, wci: Any, wcf: Any, wco: Any, b: Any, i: Any, cs: Any, f: Any, o: Any, ci: Any, co: Any, cs_grad: Any, h_grad: Any, use_peephole: Any, name: Any, ctx: Any): ...
