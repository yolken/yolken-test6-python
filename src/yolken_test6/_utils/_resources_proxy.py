from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `yolken_test6.resources` module.

    This is used so that we can lazily import `yolken_test6.resources` only when
    needed *and* so that users can just import `yolken_test6` and reference `yolken_test6.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("yolken_test6.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
