from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import reduce_util as reduce_util, values as values
from tensorflow.python.eager import backprop as backprop, context as context, def_function as def_function, test as test
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops, test_util as test_util
from tensorflow.python.keras.layers import core as core
from tensorflow.python.lib.io import tf_record as tf_record
from tensorflow.python.ops import array_ops as array_ops, gradients_impl as gradients_impl, init_ops as init_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.training import optimizer as optimizer, training_util as training_util
from tensorflow.python.util import nest as nest

class _TestException(Exception): ...
class DistributionTestBase(test.TestCase): ...
class OneDeviceDistributionTestBase(test.TestCase): ...
class TwoDeviceDistributionTestBase(test.TestCase): ...
class RemoteSingleWorkerMirroredStrategyBase(DistributionTestBase): ...
