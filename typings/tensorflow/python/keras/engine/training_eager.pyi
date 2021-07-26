from tensorflow.python.eager.backprop import GradientTape as GradientTape
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import training_utils as training_utils
from tensorflow.python.keras.mixed_precision.experimental import loss_scale_optimizer as loss_scale_optimizer
from tensorflow.python.keras.utils import losses_utils as losses_utils
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any, Optional

def train_on_batch(model: Any, inputs: Any, targets: Any, sample_weights: Optional[Any] = ..., output_loss_metrics: Optional[Any] = ...): ...
def test_on_batch(model: Any, inputs: Any, targets: Any, sample_weights: Optional[Any] = ..., output_loss_metrics: Optional[Any] = ...): ...
