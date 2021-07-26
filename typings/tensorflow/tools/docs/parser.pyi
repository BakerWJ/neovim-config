from collections import namedtuple
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any

def is_free_function(py_object: Any, full_name: Any, index: Any): ...

IDENTIFIER_RE: str

class TFDocsError(Exception): ...

class _Errors:
    def __init__(self) -> None: ...
    def log_all(self) -> None: ...
    def append(self, full_name: Any, message: Any) -> None: ...
    def __len__(self): ...
    def __eq__(self, other: Any) -> Any: ...

def documentation_path(full_name: Any, is_fragment: bool = ...): ...

SYMBOL_REFERENCE_RE: Any
AUTO_REFERENCE_RE: Any

class ReferenceResolver:
    current_doc_full_name: Any = ...
    def __init__(self, duplicate_of: Any, doc_index: Any, is_fragment: Any, py_module_names: Any) -> None: ...
    def add_error(self, message: Any) -> None: ...
    def log_errors(self) -> None: ...
    def num_errors(self): ...
    @classmethod
    def from_visitor(cls, visitor: Any, doc_index: Any, **kwargs: Any): ...
    @classmethod
    def from_json_file(cls, filepath: Any, doc_index: Any): ...
    def to_json_file(self, filepath: Any) -> None: ...
    def replace_references(self, string: Any, relative_path_to_root: Any): ...
    def python_link(self, link_text: Any, ref_full_name: Any, relative_path_to_root: Any, code_ref: bool = ...): ...
    def py_master_name(self, full_name: Any): ...
    def reference_to_url(self, ref_full_name: Any, relative_path_to_root: Any): ...

class _FunctionDetail: ...

_DocstringInfo = namedtuple('_DocstringInfo', ['brief', 'docstring', 'function_details', 'compatibility'])
PAREN_NUMBER_RE: Any

class _LinkInfo:
    def is_link(self): ...

class _OtherMemberInfo:
    def is_link(self): ...

_PropertyInfo = namedtuple('_PropertyInfo', ['short_name', 'full_name', 'obj', 'doc'])

_MethodInfo = namedtuple('_MethodInfo', ['short_name', 'full_name', 'obj', 'doc', 'signature', 'decorators'])

class _FunctionPageInfo:
    def __init__(self, full_name: Any) -> None: ...
    def for_function(self): ...
    def for_class(self): ...
    def for_module(self): ...
    @property
    def full_name(self): ...
    @property
    def short_name(self): ...
    @property
    def defined_in(self): ...
    def set_defined_in(self, defined_in: Any) -> None: ...
    @property
    def aliases(self): ...
    def set_aliases(self, aliases: Any) -> None: ...
    @property
    def doc(self): ...
    def set_doc(self, doc: Any) -> None: ...
    @property
    def guides(self): ...
    def set_guides(self, guides: Any) -> None: ...
    @property
    def signature(self): ...
    def set_signature(self, function: Any, reverse_index: Any) -> None: ...
    @property
    def decorators(self): ...
    def add_decorator(self, dec: Any) -> None: ...
    def get_metadata_html(self): ...

class _ClassPageInfo:
    def __init__(self, full_name: Any) -> None: ...
    def for_function(self): ...
    def for_class(self): ...
    def for_module(self): ...
    @property
    def full_name(self): ...
    @property
    def short_name(self): ...
    @property
    def defined_in(self): ...
    def set_defined_in(self, defined_in: Any) -> None: ...
    @property
    def aliases(self): ...
    def set_aliases(self, aliases: Any) -> None: ...
    @property
    def doc(self): ...
    def set_doc(self, doc: Any) -> None: ...
    @property
    def guides(self): ...
    def set_guides(self, guides: Any) -> None: ...
    @property
    def namedtuplefields(self): ...
    def set_namedtuplefields(self, py_class: Any) -> None: ...
    @property
    def bases(self): ...
    @property
    def properties(self): ...
    @property
    def methods(self): ...
    @property
    def classes(self): ...
    def get_metadata_html(self): ...
    @property
    def other_members(self): ...
    def collect_docs_for_class(self, py_class: Any, parser_config: Any) -> None: ...

class _ModulePageInfo:
    def __init__(self, full_name: Any) -> None: ...
    def for_function(self): ...
    def for_class(self): ...
    def for_module(self): ...
    @property
    def full_name(self): ...
    @property
    def short_name(self): ...
    @property
    def defined_in(self): ...
    def set_defined_in(self, defined_in: Any) -> None: ...
    @property
    def aliases(self): ...
    def set_aliases(self, aliases: Any) -> None: ...
    @property
    def doc(self): ...
    def set_doc(self, doc: Any) -> None: ...
    @property
    def guides(self): ...
    def set_guides(self, guides: Any) -> None: ...
    @property
    def modules(self): ...
    @property
    def classes(self): ...
    @property
    def functions(self): ...
    @property
    def other_members(self): ...
    def get_metadata_html(self): ...
    def collect_docs_for_module(self, parser_config: Any) -> None: ...

class ParserConfig:
    reference_resolver: Any = ...
    duplicates: Any = ...
    duplicate_of: Any = ...
    tree: Any = ...
    reverse_index: Any = ...
    index: Any = ...
    guide_index: Any = ...
    base_dir: Any = ...
    defined_in_prefix: str = ...
    code_url_prefix: str = ...
    def __init__(self, reference_resolver: Any, duplicates: Any, duplicate_of: Any, tree: Any, index: Any, reverse_index: Any, guide_index: Any, base_dir: Any) -> None: ...
    def py_name_to_object(self, full_name: Any): ...

def docs_for_object(full_name: Any, py_object: Any, parser_config: Any): ...

class _PythonBuiltin:
    def is_builtin(self): ...
    def is_python_file(self): ...
    def is_generated_file(self): ...

class _PythonFile:
    path: Any = ...
    path_prefix: Any = ...
    code_url_prefix: Any = ...
    def __init__(self, path: Any, parser_config: Any) -> None: ...
    def is_builtin(self): ...
    def is_python_file(self): ...
    def is_generated_file(self): ...

class _ProtoFile:
    path: Any = ...
    path_prefix: Any = ...
    code_url_prefix: Any = ...
    def __init__(self, path: Any, parser_config: Any) -> None: ...
    def is_builtin(self): ...
    def is_python_file(self): ...
    def is_generated_file(self): ...

class _GeneratedFile:
    path: Any = ...
    path_prefix: Any = ...
    def __init__(self, path: Any, parser_config: Any) -> None: ...
    def is_builtin(self): ...
    def is_python_file(self): ...
    def is_generated_file(self): ...

def generate_global_index(library_name: Any, index: Any, reference_resolver: Any): ...

class _Metadata:
    name: Any = ...
    version: Any = ...
    def __init__(self, name: Any, version: str = ...) -> None: ...
    def append(self, item: Any) -> None: ...
    def build_html(self): ...
