from typing import Any, Dict, List

class tensorflow::grappler::GrapplerItem:
    def __init__(self, *args, **kwargs) -> None: ...

def TF_GetColocationGroups(arg0) -> List[List[str]]: ...
def TF_GetOpProperties(arg0) -> Dict[str,List[bytes]]: ...
def TF_IdentifyImportantOps(arg0, arg1: bool) -> List[str]: ...
def TF_NewItem(*args, **kwargs) -> Any: ...