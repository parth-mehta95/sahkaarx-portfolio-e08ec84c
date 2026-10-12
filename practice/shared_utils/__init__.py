"""
shared_utils
~~~~~~~~~~~~

A shared Python utility package providing common helper functions for teams and services.
"""

from .string_utils import (
    slugify,
    truncate_words,
    camel_to_snake,
    snake_to_camel,
)

__version__ = "0.1.0"
__all__ = [
    "slugify",
    "truncate_words",
    "camel_to_snake",
    "snake_to_camel",
]
