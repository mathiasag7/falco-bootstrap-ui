from __future__ import annotations

from django import template
from typing import Callable

register = template.Library()

try:
    from heroicons.templatetags.heroicons import (
        heroicon_outline,
        heroicon_mini,
        heroicon_micro,
        heroicon_solid,
    )
except ImportError:
    pass
else:

    @register.simple_tag
    def heroicon_wrapper(style: str, attrs: str | None = None):
        style_tag_map: dict[str, Callable] = {
            "outline": heroicon_outline,
            "solid": heroicon_solid,
            "mini": heroicon_mini,
            "micro": heroicon_micro,
        }
        parsed_attrs = {}
        if attrs:
            parsed_attrs = dict([attr.split("=") for attr in attrs.split()])
            parsed_attrs = {k: v.strip('"') for k, v in parsed_attrs.items()}
        return style_tag_map[style](**parsed_attrs)
