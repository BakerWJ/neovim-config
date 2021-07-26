from collections import namedtuple
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional

_AllCandidateSamplerOutput = namedtuple('AllCandidateSampler', ['sampled_candidates', 'true_expected_count', 'sampled_expected_count'])

def all_candidate_sampler(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

AllCandidateSampler: Any

def all_candidate_sampler_eager_fallback(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_ComputeAccidentalHitsOutput = namedtuple('ComputeAccidentalHits', ['indices', 'ids', 'weights'])

def compute_accidental_hits(true_classes: Any, sampled_candidates: Any, num_true: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

ComputeAccidentalHits: Any

def compute_accidental_hits_eager_fallback(true_classes: Any, sampled_candidates: Any, num_true: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_FixedUnigramCandidateSamplerOutput = namedtuple('FixedUnigramCandidateSampler', ['sampled_candidates', 'true_expected_count', 'sampled_expected_count'])

def fixed_unigram_candidate_sampler(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, vocab_file: str = ..., distortion: int = ..., num_reserved_ids: int = ..., num_shards: int = ..., shard: int = ..., unigrams: Any = ..., seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

FixedUnigramCandidateSampler: Any

def fixed_unigram_candidate_sampler_eager_fallback(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, vocab_file: Any, distortion: Any, num_reserved_ids: Any, num_shards: Any, shard: Any, unigrams: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_LearnedUnigramCandidateSamplerOutput = namedtuple('LearnedUnigramCandidateSampler', ['sampled_candidates', 'true_expected_count', 'sampled_expected_count'])

def learned_unigram_candidate_sampler(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

LearnedUnigramCandidateSampler: Any

def learned_unigram_candidate_sampler_eager_fallback(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_LogUniformCandidateSamplerOutput = namedtuple('LogUniformCandidateSampler', ['sampled_candidates', 'true_expected_count', 'sampled_expected_count'])

def log_uniform_candidate_sampler(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

LogUniformCandidateSampler: Any

def log_uniform_candidate_sampler_eager_fallback(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_ThreadUnsafeUnigramCandidateSamplerOutput = namedtuple('ThreadUnsafeUnigramCandidateSampler', ['sampled_candidates', 'true_expected_count', 'sampled_expected_count'])

def thread_unsafe_unigram_candidate_sampler(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

ThreadUnsafeUnigramCandidateSampler: Any

def thread_unsafe_unigram_candidate_sampler_eager_fallback(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...

_UniformCandidateSamplerOutput = namedtuple('UniformCandidateSampler', ['sampled_candidates', 'true_expected_count', 'sampled_expected_count'])

def uniform_candidate_sampler(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: int = ..., seed2: int = ..., name: Optional[Any] = ...): ...

UniformCandidateSampler: Any

def uniform_candidate_sampler_eager_fallback(true_classes: Any, num_true: Any, num_sampled: Any, unique: Any, range_max: Any, seed: Any, seed2: Any, name: Any, ctx: Any): ...
