import abc
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils
from tensorflow.python.keras.losses import binary_crossentropy as binary_crossentropy, categorical_crossentropy as categorical_crossentropy, categorical_hinge as categorical_hinge, hinge as hinge, kullback_leibler_divergence as kullback_leibler_divergence, logcosh as logcosh, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_squared_error as mean_squared_error, mean_squared_logarithmic_error as mean_squared_logarithmic_error, poisson as poisson, sparse_categorical_crossentropy as sparse_categorical_crossentropy, squared_hinge as squared_hinge
from tensorflow.python.keras.saving.saved_model import metric_serialization as metric_serialization
from tensorflow.python.keras.utils import metrics_utils as metrics_utils
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object, to_list as to_list
from tensorflow.python.keras.utils.tf_utils import is_tensor_or_variable as is_tensor_or_variable
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, confusion_matrix as confusion_matrix, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, nn as nn, weights_broadcast_ops as weights_broadcast_ops
from tensorflow.python.util import nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import keras_export as keras_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any, Optional

class Metric(base_layer.Layer, metaclass=abc.ABCMeta):
    stateful: bool = ...
    built: bool = ...
    def __init__(self, name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    @property
    def dtype(self): ...
    def get_config(self): ...
    def reset_states(self) -> None: ...
    @abc.abstractmethod
    def update_state(self, *args: Any, **kwargs: Any) -> Any: ...
    @abc.abstractmethod
    def result(self) -> Any: ...
    def add_weight(self, name: Any, shape: Any = ..., aggregation: Any = ..., synchronization: Any = ..., initializer: Optional[Any] = ..., dtype: Optional[Any] = ...): ...

class Reduce(Metric):
    reduction: Any = ...
    total: Any = ...
    count: Any = ...
    def __init__(self, reduction: Any, name: Any, dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, values: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...

class Sum(Reduce):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class Mean(Reduce):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class MeanRelativeError(Mean):
    normalizer: Any = ...
    def __init__(self, normalizer: Any, name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def get_config(self): ...

class MeanMetricWrapper(Mean):
    def __init__(self, fn: Any, name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: Any): ...

class Accuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class BinaryAccuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ..., threshold: float = ...) -> None: ...

class CategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class SparseCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class TopKCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, k: int = ..., name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class SparseTopKCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, k: int = ..., name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class _ConfusionMatrixConditionCount(Metric):
    init_thresholds: Any = ...
    thresholds: Any = ...
    accumulator: Any = ...
    def __init__(self, confusion_matrix_cond: Any, thresholds: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...
    def reset_states(self) -> None: ...
    def get_config(self): ...

class FalsePositives(_ConfusionMatrixConditionCount):
    def __init__(self, thresholds: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...

class FalseNegatives(_ConfusionMatrixConditionCount):
    def __init__(self, thresholds: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...

class TrueNegatives(_ConfusionMatrixConditionCount):
    def __init__(self, thresholds: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...

class TruePositives(_ConfusionMatrixConditionCount):
    def __init__(self, thresholds: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...

class Precision(Metric):
    init_thresholds: Any = ...
    top_k: Any = ...
    class_id: Any = ...
    thresholds: Any = ...
    true_positives: Any = ...
    false_positives: Any = ...
    def __init__(self, thresholds: Optional[Any] = ..., top_k: Optional[Any] = ..., class_id: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...
    def reset_states(self) -> None: ...
    def get_config(self): ...

class Recall(Metric):
    init_thresholds: Any = ...
    top_k: Any = ...
    class_id: Any = ...
    thresholds: Any = ...
    true_positives: Any = ...
    false_negatives: Any = ...
    def __init__(self, thresholds: Optional[Any] = ..., top_k: Optional[Any] = ..., class_id: Optional[Any] = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...
    def reset_states(self) -> None: ...
    def get_config(self): ...

class SensitivitySpecificityBase(Metric, metaclass=abc.ABCMeta):
    value: Any = ...
    true_positives: Any = ...
    true_negatives: Any = ...
    false_positives: Any = ...
    false_negatives: Any = ...
    thresholds: Any = ...
    def __init__(self, value: Any, num_thresholds: int = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def reset_states(self) -> None: ...

class SensitivityAtSpecificity(SensitivitySpecificityBase):
    specificity: Any = ...
    num_thresholds: Any = ...
    def __init__(self, specificity: Any, num_thresholds: int = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def result(self): ...
    def get_config(self): ...

class SpecificityAtSensitivity(SensitivitySpecificityBase):
    sensitivity: Any = ...
    num_thresholds: Any = ...
    def __init__(self, sensitivity: Any, num_thresholds: int = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def result(self): ...
    def get_config(self): ...

class PrecisionAtRecall(SensitivitySpecificityBase):
    recall: Any = ...
    num_thresholds: Any = ...
    def __init__(self, recall: Any, num_thresholds: int = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def result(self): ...
    def get_config(self): ...

class RecallAtPrecision(SensitivitySpecificityBase):
    precision: Any = ...
    num_thresholds: Any = ...
    def __init__(self, precision: Any, num_thresholds: int = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def result(self): ...
    def get_config(self): ...

class AUC(Metric):
    num_thresholds: Any = ...
    thresholds: Any = ...
    curve: Any = ...
    summation_method: Any = ...
    multi_label: Any = ...
    label_weights: Any = ...
    def __init__(self, num_thresholds: int = ..., curve: str = ..., summation_method: str = ..., name: Optional[Any] = ..., dtype: Optional[Any] = ..., thresholds: Optional[Any] = ..., multi_label: bool = ..., label_weights: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def interpolate_pr_auc(self): ...
    def result(self): ...
    def reset_states(self) -> None: ...
    def get_config(self): ...

class CosineSimilarity(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ..., axis: int = ...) -> None: ...

class MeanAbsoluteError(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class MeanAbsolutePercentageError(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class MeanSquaredError(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class MeanSquaredLogarithmicError(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class Hinge(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class SquaredHinge(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class CategoricalHinge(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class RootMeanSquaredError(Mean):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...

class LogCoshError(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class Poisson(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class KLDivergence(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class MeanIoU(Metric):
    num_classes: Any = ...
    total_cm: Any = ...
    def __init__(self, num_classes: Any, name: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...
    def reset_states(self) -> None: ...
    def get_config(self): ...

class MeanTensor(Metric):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...
    @property
    def total(self): ...
    @property
    def count(self): ...
    def update_state(self, values: Any, sample_weight: Optional[Any] = ...): ...
    def result(self): ...
    def reset_states(self) -> None: ...

class BinaryCrossentropy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ..., from_logits: bool = ..., label_smoothing: int = ...) -> None: ...

class CategoricalCrossentropy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ..., from_logits: bool = ..., label_smoothing: int = ...) -> None: ...

class SparseCategoricalCrossentropy(MeanMetricWrapper):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ..., from_logits: bool = ..., axis: int = ...) -> None: ...

class SumOverBatchSize(Reduce):
    def __init__(self, name: str = ..., dtype: Optional[Any] = ...) -> None: ...

class SumOverBatchSizeMetricWrapper(SumOverBatchSize):
    def __init__(self, fn: Any, name: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def update_state(self, y_true: Any, y_pred: Any, sample_weight: Optional[Any] = ...): ...
    def get_config(self): ...

def accuracy(y_true: Any, y_pred: Any): ...
def binary_accuracy(y_true: Any, y_pred: Any, threshold: float = ...): ...
def categorical_accuracy(y_true: Any, y_pred: Any): ...
def sparse_categorical_accuracy(y_true: Any, y_pred: Any): ...
def top_k_categorical_accuracy(y_true: Any, y_pred: Any, k: int = ...): ...
def sparse_top_k_categorical_accuracy(y_true: Any, y_pred: Any, k: int = ...): ...
def cosine_proximity(y_true: Any, y_pred: Any, axis: int = ...): ...
acc = accuracy
ACC = accuracy
bce = binary_crossentropy
BCE = binary_crossentropy
mse = mean_squared_error
MSE = mean_squared_error
mae = mean_absolute_error
MAE = mean_absolute_error
mape = mean_absolute_percentage_error
MAPE = mean_absolute_percentage_error
msle = mean_squared_logarithmic_error
MSLE = mean_squared_logarithmic_error
cosine_similarity = cosine_proximity

def clone_metric(metric: Any): ...
def clone_metrics(metrics: Any): ...
def serialize(metric: Any): ...
def deserialize(config: Any, custom_objects: Optional[Any] = ...): ...
def get(identifier: Any): ...
def is_built_in(cls): ...