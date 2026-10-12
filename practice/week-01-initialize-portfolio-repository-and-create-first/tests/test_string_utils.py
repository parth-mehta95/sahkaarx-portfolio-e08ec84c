"""
Unit tests for shared_utils.string_utils.
"""

import unittest
from shared_utils.string_utils import (
    slugify,
    truncate_words,
    camel_to_snake,
    snake_to_camel,
    mask_sensitive,
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


class TestCamelToSnake(unittest.TestCase):
    """Test suite for camel_to_snake utility function."""

    def test_camel_to_snake_conversion(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake("PascalCase"), "pascal_case")
        self.assertEqual(camel_to_snake("HTTPRequestParser"), "http_request_parser")
        self.assertEqual(camel_to_snake("simple"), "simple")
        self.assertEqual(camel_to_snake(""), "")


class TestSnakeToCamel(unittest.TestCase):
    """Test suite for snake_to_camel utility function."""

    def test_snake_to_camel_conversion(self):
        self.assertEqual(snake_to_camel("snake_case"), "snakeCase")
        self.assertEqual(snake_to_camel("snake_case", capitalize_first=True), "SnakeCase")
        self.assertEqual(snake_to_camel("simple"), "simple")
        self.assertEqual(snake_to_camel(""), "")


class TestMaskSensitive(unittest.TestCase):
    """Test suite for mask_sensitive utility function."""

    def test_default_masking(self):
        # Default: visible_start=0, visible_end=4, mask_char='*'
        self.assertEqual(
            mask_sensitive("1234567812345678"),
            "************5678",
        )
        self.assertEqual(mask_sensitive("hello world"), "*******orld")

    def test_custom_visible_counts(self):
        self.assertEqual(
            mask_sensitive("user@example.com", visible_start=2, visible_end=4),
            "us**********com",
        )
        self.assertEqual(
            mask_sensitive("ABCDEFGHIJ", visible_start=3, visible_end=2),
            "ABC*****IJ",
        )

    def test_custom_mask_char(self):
        self.assertEqual(
            mask_sensitive("secret-token-key", visible_start=2, visible_end=2, mask_char="#"),
            "se############ey",
        )
        self.assertEqual(
            mask_sensitive("12345678", visible_start=1, visible_end=1, mask_char="X"),
            "1XXXXXX8",
        )

    def test_visible_counts_exceeding_or_equal_length(self):
        # When visible_start + visible_end >= text length, return string unchanged
        self.assertEqual(mask_sensitive("short", visible_start=3, visible_end=3), "short")
        self.assertEqual(mask_sensitive("exact", visible_start=2, visible_end=3), "exact")

    def test_empty_string(self):
        self.assertEqual(mask_sensitive(""), "")

    def test_negative_counts_raise_error(self):
        with self.assertRaises(ValueError):
            mask_sensitive("test", visible_start=-1)
        with self.assertRaises(ValueError):
            mask_sensitive("test", visible_end=-1)

    def test_invalid_mask_char_length_raises_error(self):
        with self.assertRaises(ValueError):
            mask_sensitive("test", mask_char="**")
        with self.assertRaises(ValueError):
            mask_sensitive("test", mask_char="")

    def test_invalid_types_raise_error(self):
        with self.assertRaises(TypeError):
            mask_sensitive(12345)  # type: ignore
        with self.assertRaises(TypeError):
            mask_sensitive("test", visible_start=True)  # type: ignore (bool is int subclass)
        with self.assertRaises(TypeError):
            mask_sensitive("test", visible_end="four")  # type: ignore
        with self.assertRaises(TypeError):
            mask_sensitive("test", mask_char=123)  # type: ignore


if __name__ == "__main__":
    unittest.main()

