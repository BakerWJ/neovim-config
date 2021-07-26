from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors
from tensorflow.python.keras.distribute import distributed_training_utils as distributed_training_utils
from tensorflow.python.keras.engine import training_utils as training_utils
from tensorflow.python.keras.utils.generic_utils import make_batches as make_batches, slice_arrays as slice_arrays
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.util import nest as nest
from typing import Any, Optional

def model_iteration(model: Any, inputs: Any, targets: Optional[Any] = ..., sample_weights: Optional[Any] = ..., batch_size: Optional[Any] = ..., epochs: int = ..., verbose: int = ..., callbacks: Optional[Any] = ..., val_inputs: Optional[Any] = ..., val_targets: Optional[Any] = ..., val_sample_weights: Optional[Any] = ..., shuffle: bool = ..., initial_epoch: int = ..., steps_per_epoch: Optional[Any] = ..., validation_steps: Optional[Any] = ..., validation_freq: int = ..., mode: Any = ..., validation_in_fit: bool = ..., prepared_feed_values_from_dataset: bool = ..., steps_name: str = ..., **kwargs: Any): ...

fit_loop: Any
test_loop: Any
predict_loop: Any

class ArrayLikeTrainingLoop(training_utils.TrainingLoop):
    def fit(self, model: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., batch_size: Optional[Any] = ..., epochs: int = ..., verbose: int = ..., callbacks: Optional[Any] = ..., validation_split: float = ..., validation_data: Optional[Any] = ..., shuffle: bool = ..., class_weight: Optional[Any] = ..., sample_weight: Optional[Any] = ..., initial_epoch: int = ..., steps_per_epoch: Optional[Any] = ..., validation_steps: Optional[Any] = ..., validation_freq: int = ..., **kwargs: Any): ...
    def evaluate(self, model: Any, x: Optional[Any] = ..., y: Optional[Any] = ..., batch_size: Optional[Any] = ..., verbose: int = ..., sample_weight: Optional[Any] = ..., steps: Optional[Any] = ..., callbacks: Optional[Any] = ..., **kwargs: Any): ...
    def predict(self, model: Any, x: Any, batch_size: Optional[Any] = ..., verbose: int = ..., steps: Optional[Any] = ..., callbacks: Optional[Any] = ..., **kwargs: Any): ...
