from . import experimental as experimental
from tensorflow.python.debug.lib.check_numerics_callback import disable_check_numerics as disable_check_numerics, enable_check_numerics as enable_check_numerics
from tensorflow.python.eager.context import get_log_device_placement as get_log_device_placement, set_log_device_placement as set_log_device_placement
from tensorflow.python.ops.check_ops import assert_proper_iterable as assert_proper_iterable, assert_same_float_dtype as assert_same_float_dtype, is_numeric_tensor as is_numeric_tensor
from tensorflow.python.ops.control_flow_ops import Assert as Assert
from tensorflow.python.ops.gen_array_ops import check_numerics as check_numerics
