"""
Custom template tags and filters for the wiki.
"""

from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter(name='markdown')
def render_markdown(text):
    """
    Convert Markdown text to HTML.
    
    Usage in templates:
        {{ page.content|markdown }}
    """
    if not text:
        return ""
    
    # Render markdown with extensions
    html = markdown.markdown(
        text,
        extensions=[
            'extra',        # Tables, fenced code blocks, etc.
            'codehilite',   # Syntax highlighting
            'nl2br',        # Newline to <br>
            'sane_lists',   # Better list handling
        ]
    )
    
    return mark_safe(html)

