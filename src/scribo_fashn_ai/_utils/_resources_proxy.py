from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `scribo_fashn_ai.resources` module.

    This is used so that we can lazily import `scribo_fashn_ai.resources` only when
    needed *and* so that users can just import `scribo_fashn_ai` and reference `scribo_fashn_ai.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("scribo_fashn_ai.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
