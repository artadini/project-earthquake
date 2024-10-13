import unittest
from unittest.mock import patch, MagicMock
from functions.transformation import validate_and_transform_schema


class ValidateAndTransformSchema(unittest.TestCase):
    """
    Unit tests for the validate_and_transform_schema function.

    Test Cases:
        - test_validate_and_transform_schema: Tests the transformation of schema and data rows.
            - Mocks the logger used in the transformation function.
            - Defines an extracted schema and an expected schema.
            - Defines data rows to be transformed.
            - Asserts that the extracted schema is transformed to match the expected schema.
            - Asserts that the data rows are transformed correctly to match the expected schema.
    """

    @patch("functions.transformation.get_logger")
    def test_validate_and_transform_schema(self, mock_get_logger):
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        extracted_schema = {"id": "string", "value": "int64"}
        expected_schema = {"id": "string", "value": "float64"}
        data_rows = [{"id": "1", "value": "10"}, {"id": "2", "value": "20"}]

        validate_and_transform_schema(extracted_schema, expected_schema, data_rows)

        self.assertEqual(extracted_schema["value"], "float64")
        self.assertEqual(data_rows[0]["value"], 10.0)
        self.assertEqual(data_rows[1]["value"], 20.0)


if __name__ == "__main__":
    unittest.main()
