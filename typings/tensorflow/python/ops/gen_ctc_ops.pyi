from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_CTCBeamSearchDecoderOutput = namedtuple('CTCBeamSearchDecoder', ['decoded_indices', 'decoded_values', 'decoded_shape', 'log_probability'])

def ctc_beam_search_decoder(inputs: Any, sequence_length: Any, beam_width: Any, top_paths: Any, merge_repeated: bool = ..., name: Optional[Any] = ...): ...

CTCBeamSearchDecoder: Any

def ctc_beam_search_decoder_eager_fallback(inputs: Any, sequence_length: Any, beam_width: Any, top_paths: Any, merge_repeated: Any, name: Any, ctx: Any): ...

_CTCGreedyDecoderOutput = namedtuple('CTCGreedyDecoder', ['decoded_indices', 'decoded_values', 'decoded_shape', 'log_probability'])

def ctc_greedy_decoder(inputs: Any, sequence_length: Any, merge_repeated: bool = ..., name: Optional[Any] = ...): ...

CTCGreedyDecoder: Any

def ctc_greedy_decoder_eager_fallback(inputs: Any, sequence_length: Any, merge_repeated: Any, name: Any, ctx: Any): ...

_CTCLossOutput = namedtuple('CTCLoss', ['loss', 'gradient'])

def ctc_loss(inputs: Any, labels_indices: Any, labels_values: Any, sequence_length: Any, preprocess_collapse_repeated: bool = ..., ctc_merge_repeated: bool = ..., ignore_longer_outputs_than_inputs: bool = ..., name: Optional[Any] = ...): ...

CTCLoss: Any

def ctc_loss_eager_fallback(inputs: Any, labels_indices: Any, labels_values: Any, sequence_length: Any, preprocess_collapse_repeated: Any, ctc_merge_repeated: Any, ignore_longer_outputs_than_inputs: Any, name: Any, ctx: Any): ...

_CTCLossV2Output = namedtuple('CTCLossV2', ['loss', 'gradient'])

def ctc_loss_v2(inputs: Any, labels_indices: Any, labels_values: Any, sequence_length: Any, preprocess_collapse_repeated: bool = ..., ctc_merge_repeated: bool = ..., ignore_longer_outputs_than_inputs: bool = ..., name: Optional[Any] = ...): ...

CTCLossV2: Any

def ctc_loss_v2_eager_fallback(inputs: Any, labels_indices: Any, labels_values: Any, sequence_length: Any, preprocess_collapse_repeated: Any, ctc_merge_repeated: Any, ignore_longer_outputs_than_inputs: Any, name: Any, ctx: Any): ...
