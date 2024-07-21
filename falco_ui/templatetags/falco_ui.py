from __future__ import annotations

from django import template
from django.templatetags.static import static
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def falco_ui_script(
    alpinejs: str = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js",
) -> str:
    return format_html(
        '<script src="{}" defer></script>\n<script src="{}"></script>',
        alpinejs,
        static("falco-ui/main.js"),
    )


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
        style_tag_map: dict[str, callable] = {
            "outline": heroicon_outline,
            "solid": heroicon_solid,
            "mini": heroicon_mini,
            "micro": heroicon_micro,
        }
        if attrs is None:
            attrs = {}
        else:
            attrs = dict([attr.split("=") for attr in attrs.split()])
            attrs = {k: v.strip('"') for k, v in attrs.items()}
        return style_tag_map[style](**attrs)
