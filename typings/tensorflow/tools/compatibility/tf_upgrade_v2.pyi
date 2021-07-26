from tensorflow.tools.compatibility import all_renames_v2 as all_renames_v2, ast_edits as ast_edits, module_deprecations_v2 as module_deprecations_v2, reorders_v2 as reorders_v2
from typing import Any

class UnaliasedTFImport(ast_edits.AnalysisResult):
    log_level: Any = ...
    log_message: str = ...
    def __init__(self) -> None: ...

class VersionedTFImport(ast_edits.AnalysisResult):
    log_level: Any = ...
    log_message: Any = ...
    def __init__(self, version: Any) -> None: ...

class TFAPIImportAnalysisSpec(ast_edits.APIAnalysisSpec):
    symbols_to_detect: Any = ...
    imports_to_detect: Any = ...
    def __init__(self) -> None: ...

class TFAPIChangeSpec(ast_edits.NoUpdateSpec):
    function_keyword_renames: Any = ...
    symbol_renames: Any = ...
    import_rename: Any = ...
    import_renames: Any = ...
    change_to_function: Any = ...
    reordered_function_names: Any = ...
    manual_function_reorders: Any = ...
    function_reorders: Any = ...
    function_warnings: Any = ...
    function_arg_warnings: Any = ...
    function_transformers: Any = ...
    module_deprecations: Any = ...
    def __init__(self, import_rename: bool = ...) -> None: ...
    function_handle: Any = ...
    def preprocess(self, root_node: Any): ...
    def clear_preprocessing(self) -> None: ...
