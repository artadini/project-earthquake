import unittest
from functions.transformation import determine_type, convert_to_type


class TypeTests(unittest.TestCase):
    """
    Unit tests for type determination and conversion functions.

    Test Cases:
        - test_determine_type_int: Verify that a numeric string is identified as an integer type.
        - test_determine_type_float: Verify that a numeric string with a decimal point is identified as a float type.
        - test_determine_type_string: Verify that a non-numeric string is identified as a string type.
        - test_determine_type_negative_int: Verify that a negative numeric string is identified as an integer type.
        - test_determine_type_negative_float: Verify that a negative numeric string with a decimal point is identified as a float type.
        - test_determine_type_empty_string: Verify that an empty string is identified as a string type.
        - test_determine_type_whitespace: Verify that a whitespace string is identified as a string type.
        - test_determine_type_mixed: Verify that a mixed alphanumeric string is identified as a string type.
        - test_convert_to_type_int: Verify that a numeric string can be converted to an integer.
        - test_convert_to_type_float: Verify that a numeric string with a decimal point can be converted to a float.
        - test_convert_to_type_string: Verify that a non-numeric string can be converted to a string.
        - test_convert_to_type_invalid_int: Verify that converting a non-numeric string to an integer raises a ValueError.
        - test_convert_to_type_invalid_float: Verify that converting a non-numeric string to a float raises a ValueError.
    """

    def test_determine_type_int(self):
        self.assertEqual(determine_type("123"), "int64")

    def test_determine_type_float(self):
        self.assertEqual(determine_type("123.45"), "float64")

    def test_determine_type_string(self):
        self.assertEqual(determine_type("abc"), "string")

    def test_determine_type_negative_int(self):
        self.assertEqual(determine_type("-123"), "int64")  # Updated to int64

    def test_determine_type_negative_float(self):
        self.assertEqual(determine_type("-123.45"), "float64")

    def test_determine_type_empty_string(self):
        self.assertEqual(determine_type(""), "string")

    def test_determine_type_whitespace(self):
        self.assertEqual(determine_type("   "), "string")

    def test_determine_type_mixed(self):
        self.assertEqual(determine_type("123abc"), "string")

    def test_convert_to_type_int(self):
        self.assertEqual(convert_to_type("123", "int64"), 123)

    def test_convert_to_type_float(self):
        self.assertEqual(convert_to_type("123.45", "float64"), 123.45)

    def test_convert_to_type_string(self):
        self.assertEqual(convert_to_type("abc", "string"), "abc")

    def test_convert_to_type_invalid_int(self):
        with self.assertRaises(ValueError):
            convert_to_type("abc", "int64")

    def test_convert_to_type_invalid_float(self):
        with self.assertRaises(ValueError):
            convert_to_type("abc", "float64")


if __name__ == "__main__":
    unittest.main()
