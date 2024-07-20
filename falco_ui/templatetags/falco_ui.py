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
