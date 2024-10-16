import unittest
from unittest.mock import patch, MagicMock
from functions.extraction import get_coordinates


class GetCoordinates(unittest.TestCase):
    """
    Unit tests for the get_coordinates function.

    Methods:
        test_get_coordinates(self, MockArcGIS):
            Tests the get_coordinates function with valid locations.
            Mocks the ArcGIS geocode method to return predefined coordinates for Los Angeles and New York.
            Asserts that the function returns the expected output.

        test_get_coordinates_with_missing_location(self, MockArcGIS):
            Tests the get_coordinates function with a missing location.
            Mocks the ArcGIS geocode method to return None for an unknown location and predefined coordinates for New York.
            Asserts that the function returns the expected output, excluding the missing location.
    """

    @patch("functions.extraction.ArcGIS")
    def test_get_coordinates(self, MockArcGIS):
        # Mock the geocode method
        mock_geocode = MagicMock()
        mock_geocode.side_effect = [
            MagicMock(latitude=34.0522, longitude=-118.2437),  # Los Angeles
            MagicMock(latitude=40.7128, longitude=-74.0060),  # New York
        ]
        MockArcGIS.return_value.geocode = mock_geocode

        # Define the input dictionary
        locations = {"Los Angeles": "Los Angeles, CA", "New York": "New York, NY"}

        # Expected output
        expected_output = {
            "Los Angeles": [34.0522, -118.2437],
            "New York": [40.7128, -74.0060],
        }

        # Call the function
        result = get_coordinates(locations)

        # Assert the result
        self.assertEqual(result, expected_output)

    @patch("functions.extraction.ArcGIS")
    def test_get_coordinates_with_missing_location(self, MockArcGIS):
        # Mock the geocode method
        mock_geocode = MagicMock()
        mock_geocode.side_effect = [
            None,  # Missing location
            MagicMock(latitude=40.7128, longitude=-74.0060),  # New York
        ]
        MockArcGIS.return_value.geocode = mock_geocode

        # Define the input dictionary
        locations = {"Unknown": "Unknown, XX", "New York": "New York, NY"}

        # Expected output
        expected_output = {"New York": [40.7128, -74.0060]}

        # Call the function
        result = get_coordinates(locations)

        # Assert the result
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
