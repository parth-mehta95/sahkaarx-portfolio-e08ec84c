"""
Unit tests for shared_utils.string_utils incorporating code review feedback.
"""

import unittest
from shared_utils.string_utils import (
    slugify,
    truncate_words,
    camel_to_snake,
    snake_to_camel,
)


class TestSlugify(unittest.TestCase):
    """Test suite for slugify utility function."""

    def test_basic_slugify(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
        self.assertEqual(slugify("Python 3.12 Rocks"), "python-312-rocks")

    def test_punctuation_and_special_characters(self):
        self.assertEqual(
            slugify("Hello, World! #2026 @team"),
            "hello-world-2026-team",
        )
        self.assertEqual(slugify("---Leading and trailing---"), "leading-and-trailing")

    def test_multiple_spaces_and_separators(self):
        self.assertEqual(slugify("Multiple   spaces    here"), "multiple-spaces-here")
        self.assertEqual(slugify("Mixed -- spaces - and - dashes"), "mixed-spaces-and-dashes")

    def test_custom_separator(self):
        self.assertEqual(slugify("Custom Separator Test", separator="_"), "custom_separator_test")
        self.assertEqual(slugify("Dot.Separated.String", separator="."), "dotseparatedstring")

    def test_unicode_handling(self):
        # ASCII fallback
        self.assertEqual(slugify("Café au lait"), "cafe-au-lait")
        # Unicode allowed
        self.assertEqual(slugify("Café au lait", allow_unicode=True), "café-au-lait")

    def test_empty_and_whitespace_only(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("   "), "")

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            slugify(12345)  # type: ignore


class TestTruncateWords(unittest.TestCase):
    """Test suite for truncate_words utility function."""

    def test_truncation_under_limit(self):
        text = "Short sentence"
        self.assertEqual(truncate_words(text, 5), "Short sentence")

    def test_truncation_exact_limit(self):
        text = "Exact four words here"
        self.assertEqual(truncate_words(text, 4), "Exact four words here")

    def test_truncation_over_limit(self):
        text = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(truncate_words(text, 4), "The quick brown fox...")

    def test_custom_suffix(self):
        text = "One two three four"
        self.assertEqual(truncate_words(text, 2, suffix=" [more]"), "One two [more]")

    def test_zero_words(self):
        text = "One two three"
        self.assertEqual(truncate_words(text, 0), "...")

    def test_negative_limit_raises_error(self):
        with self.assertRaises(ValueError):
            truncate_words("Hello", -1)

    def test_invalid_types_raise_error(self):
        with self.assertRaises(TypeError):
            truncate_words(12345, 2)  # type: ignore
        with self.assertRaises(TypeError):
            truncate_words("Hello world", "two")  # type: ignore
        with self.assertRaises(TypeError):
            truncate_words("Hello world", True)  # type: ignore


class TestCamelToSnake(unittest.TestCase):
    """Test suite for camel_to_snake utility function."""

    def test_camel_to_snake_conversion(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake("PascalCase"), "pascal_case")
        self.assertEqual(camel_to_snake("HTTPRequestParser"), "http_request_parser")
        self.assertEqual(camel_to_snake("simple"), "simple")
        self.assertEqual(camel_to_snake(""), "")

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            camel_to_snake(None)  # type: ignore


class TestSnakeToCamel(unittest.TestCase):
    """Test suite for snake_to_camel utility function."""

    def test_snake_to_camel_conversion(self):
        self.assertEqual(snake_to_camel("snake_case"), "snakeCase")
        self.assertEqual(snake_to_camel("snake_case", capitalize_first=True), "SnakeCase")
        self.assertEqual(snake_to_camel("simple"), "simple")
        self.assertEqual(snake_to_camel(""), "")

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            snake_to_camel(100)  # type: ignore


if __name__ == "__main__":
    unittest.main()
