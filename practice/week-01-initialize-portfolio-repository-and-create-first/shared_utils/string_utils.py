"""
string_utils
~~~~~~~~~~~~

Core string manipulation and formatting utility functions.
"""

import re
import unicodedata
from typing import Optional


def slugify(text: str, separator: str = "-", allow_unicode: bool = False) -> str:
    """
    Convert a string into a clean, URL-friendly slug.

    Transforms text by normalizing unicode characters, removing non-alphanumeric
    characters, converting to lowercase, and replacing whitespace and repeated
    separators with a single separator.

    Parameters:
        text (str): The input text to be converted to a slug.
        separator (str, optional): Separator character to use between words. Defaults to '-'.
        allow_unicode (bool, optional): If True, preserves non-ASCII unicode alphanumeric characters.
                                        Defaults to False.

    Returns:
        str: Cleaned and normalized slug.

    Examples:
        >>> slugify("Hello World! Welcome to Python.")
        'hello-world-welcome-to-python'
        >>> slugify("Café au lait", separator="_")
        'cafe_au_lait'
        >>> slugify("  Extra   spaces  --- and symbols ### ")
        'extra-spaces-and-symbols'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    text = str(text).strip()
    if not text:
        return ""

    if allow_unicode:
        text = unicodedata.normalize("NFKC", text)
    else:
        text = (
            unicodedata.normalize("NFKD", text)
            .encode("ascii", "ignore")
            .decode("ascii")
        )

    # Convert to lowercase
    text = text.lower()

    # Remove characters that aren't alphanumeric or whitespace/hyphens
    if allow_unicode:
        text = re.sub(r"[^\w\s-]", "", text)
    else:
        text = re.sub(r"[^a-z0-9\s-]", "", text)

    # Replace spaces and repeated hyphens with the designated separator
    escaped_sep = re.escape(separator)
    text = re.sub(r"[\s-]+", separator, text)

    # Strip leading and trailing separator
    text = re.sub(f"^{escaped_sep}+|{escaped_sep}+$", "", text)

    return text


def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum number of words, appending a suffix if truncated.

    Parameters:
        text (str): Input string.
        max_words (int): Maximum word count before truncating. Must be >= 0.
        suffix (str, optional): Suffix to append if truncated. Defaults to '...'.

    Returns:
        str: Truncated string or original string if word count is within limit.

    Raises:
        ValueError: If max_words is negative.

    Examples:
        >>> truncate_words("The quick brown fox jumps over the lazy dog", 4)
        'The quick brown fox...'
        >>> truncate_words("Short text", 5)
        'Short text'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    if max_words < 0:
        raise ValueError("max_words must be non-negative")

    words = text.strip().split()
    if len(words) <= max_words:
        return text

    if max_words == 0:
        return suffix

    return " ".join(words[:max_words]) + suffix


def camel_to_snake(name: str) -> str:
    """
    Convert a CamelCase or mixedCase string to snake_case.

    Parameters:
        name (str): The camelCase or PascalCase string.

    Returns:
        str: The converted snake_case string.

    Examples:
        >>> camel_to_snake("CamelCase")
        'camel_case'
        >>> camel_to_snake("getHTTPResponseCode")
        'get_http_response_code'
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected str, got {type(name).__name__}")

    if not name:
        return ""

    # Insert underscore between consecutive capitals followed by lowercase
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscore between lower/number and capital
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def snake_to_camel(name: str, capitalize_first: bool = False) -> str:
    """
    Convert a snake_case string to camelCase or PascalCase.

    Parameters:
        name (str): The snake_case string.
        capitalize_first (bool, optional): If True, returns PascalCase. Defaults to False (camelCase).

    Returns:
        str: Converted camelCase or PascalCase string.

    Examples:
        >>> snake_to_camel("hello_world")
        'helloWorld'
        >>> snake_to_camel("hello_world", capitalize_first=True)
        'HelloWorld'
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected str, got {type(name).__name__}")

    if not name:
        return ""

    components = name.strip("_").split("_")
    if not components or components == [""]:
        return ""

    first = components[0].capitalize() if capitalize_first else components[0].lower()
    rest = "".join(x.capitalize() for x in components[1:])
    return first + rest
