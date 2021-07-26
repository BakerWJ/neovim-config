from collections import namedtuple
from typing import Any

GpuInfo = namedtuple('gpu_info', ['name', 'compute_capability'])

def compute_capability_from_device_desc(device_attrs: Any): ...
