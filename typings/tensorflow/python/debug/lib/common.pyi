from collections import namedtuple
from typing import Any

GRPC_URL_PREFIX: str

RunKey = namedtuple('RunKey', ['feed_names', 'fetch_names'])

def get_graph_element_name(elem: Any): ...
def get_flattened_names(feeds_or_fetches: Any): ...
def get_run_key(feed_dict: Any, fetches: Any): ...
