from tensorflow.python.debug.lib import check_numerics_callback as check_numerics_callback, debug_events_reader as debug_events_reader, dumping_callback as dumping_callback
from tensorflow.python.framework import test_util as test_util, versions as versions
from typing import Any

class DumpingCallbackTestBase(test_util.TensorFlowTestCase):
    dump_root: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...