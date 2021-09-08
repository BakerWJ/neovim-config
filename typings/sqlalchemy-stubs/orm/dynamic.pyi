from typing import Any
from typing import Optional

from . import attributes as attributes
from . import interfaces as interfaces
from . import object_mapper as object_mapper
from . import object_session as object_session
from . import relationships as relationships
from . import strategies as strategies
from .query import Query as Query
from .. import exc as exc
from .. import log as log
from .. import sql as sql
from .. import util as util
from ..sql import selectable as selectable
from ..sql.base import Generative as Generative

class DynaLoader(strategies.AbstractRelationshipLoader):
    is_class_level: bool = ...
    def init_class_attribute(self, mapper: Any) -> None: ...

class DynamicAttributeImpl(attributes.AttributeImpl):
    uses_objects: bool = ...
    default_accepts_scalar_loader: bool = ...
    supports_population: bool = ...
    collection: bool = ...
    dynamic: bool = ...
    target_mapper: Any = ...
    order_by: Any = ...
    query_class: Any = ...
    def __init__(
        self,
        class_: Any,
        key: Any,
        typecallable: Any,
        dispatch: Any,
        target_mapper: Any,
        order_by: Any,
        **kw: Any,
    ) -> None: ...
    def get(self, state: Any, dict_: Any, passive: Any = ...): ...
    def get_collection(
        self,
        state: Any,
        dict_: Any,
        user_data: Optional[Any] = ...,
        passive: Any = ...,
    ): ...
    def fire_append_event(
        self,
        state: Any,
        dict_: Any,
        value: Any,
        initiator: Any,
        collection_history: Optional[Any] = ...,
    ) -> None: ...
    def fire_remove_event(
        self,
        state: Any,
        dict_: Any,
        value: Any,
        initiator: Any,
        collection_history: Optional[Any] = ...,
    ) -> None: ...
    def set(
        self,
        state: Any,
        dict_: Any,
        value: Any,
        initiator: Optional[Any] = ...,
        passive: Any = ...,
        check_old: Optional[Any] = ...,
        pop: bool = ...,
        _adapt: bool = ...,
    ) -> None: ...
    def delete(self, *args: Any, **kwargs: Any) -> None: ...
    def set_committed_value(
        self, state: Any, dict_: Any, value: Any
    ) -> None: ...
    def get_history(self, state: Any, dict_: Any, passive: Any = ...): ...
    def get_all_pending(self, state: Any, dict_: Any, passive: Any = ...): ...
    def append(
        self,
        state: Any,
        dict_: Any,
        value: Any,
        initiator: Any,
        passive: Any = ...,
    ) -> None: ...
    def remove(
        self,
        state: Any,
        dict_: Any,
        value: Any,
        initiator: Any,
        passive: Any = ...,
    ) -> None: ...
    def pop(
        self,
        state: Any,
        dict_: Any,
        value: Any,
        initiator: Any,
        passive: Any = ...,
    ) -> None: ...

class AppenderQuery(Generative):
    instance: Any = ...
    attr: Any = ...
    mapper: Any = ...
    def __init__(self, attr: Any, state: Any) -> None: ...
    def autoflush(self, setting: Any) -> None: ...
    @property
    def statement(self): ...
    def filter(self, *criteria: Any): ...
    def where(self, *criteria: Any) -> None: ...
    def order_by(self, *criteria: Any) -> None: ...
    def filter_by(self, **kwargs: Any) -> None: ...
    def join(self, target: Any, *props: Any, **kwargs: Any) -> None: ...
    def outerjoin(self, target: Any, *props: Any, **kwargs: Any) -> None: ...
    def scalar(self): ...
    def first(self): ...
    def one(self): ...
    def one_or_none(self): ...
    def all(self): ...
    def session(self): ...
    session: Any = ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, index: Any): ...
    def limit(self, limit: Any) -> None: ...
    def offset(self, offset: Any) -> None: ...
    def slice(self, start: Any, stop: Any) -> None: ...
    def count(self): ...
    def extend(self, iterator: Any) -> None: ...
    def append(self, item: Any) -> None: ...
    def remove(self, item: Any) -> None: ...

class CollectionHistory:
    unchanged_items: Any = ...
    added_items: Any = ...
    deleted_items: Any = ...
    def __init__(
        self, attr: Any, state: Any, apply_to: Optional[Any] = ...
    ) -> None: ...
    @property
    def added_plus_unchanged(self): ...
    @property
    def all_items(self): ...
    def as_history(self): ...
    def indexed(self, index: Any): ...
    def add_added(self, value: Any) -> None: ...
    def add_removed(self, value: Any) -> None: ...