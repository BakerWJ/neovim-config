from collections import namedtuple
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, test_util as test_util
from tensorflow.python.ops import nn_ops as nn_ops
from tensorflow.python.platform import test as test

LayerShapeNHWC = namedtuple('LayerShapeNHWC', 'batch, height, width, channels')

FilterShape2D = namedtuple('FilterShape2D', 'height, width, in_channels, out_channels')

LayerShapeNCDHW = namedtuple('LayerShapeNCDHW', 'batch, channels, depth, height, width')

FilterShape3D = namedtuple('FilterShape3D', 'depth, height, width, in_channels, out_channels')

class ConvolutionTest(test.TestCase):
    def testForward(self) -> None: ...
    def testBackwardFilterGradient(self) -> None: ...
    def testBackwardInputGradient(self) -> None: ...
