import datetime
import pandas as pd
from functions.logger import get_logger
import csv
from io import StringIO

logger = get_logger("transformation")


def minor_transform_and_append_dataframe(
    location_name, df, columns_to_keep, end_combined_df
):
    """
    Combines and transforms a DataFrame by adding location, timestamp, and hash ID columns,
    and optionally appends it to an existing DataFrame.

    Parameters:
    location_name (str): The name of the location to be added as a column.
    df (pd.DataFrame): The DataFrame to be transformed.
    columns_to_keep (list): List of columns to keep in the final DataFrame.
    end_combined_df (pd.DataFrame or None): The existing DataFrame to append the transformed DataFrame to.
                                            If None, only the transformed DataFrame is returned.

    Returns:
    pd.DataFrame: The transformed DataFrame with added columns and optionally combined with the existing DataFrame.
    str: A message indicating an empty response if the input DataFrame is None.
    """

    logger.info(f"Combining and transforming data for location: {location_name}")

    if df is not None:
        df["location"] = location_name  # Add a column for the location name
        df["inserted_at"] = datetime.datetime.now()  # Add a timestamp

        # Create a hash column
        df["hashed_id"] = df.apply(
            lambda x: hash(tuple(x[col] for col in df.columns if col != "id")),
            axis=1,
        )
        df.drop_duplicates(subset=["id"])  # Remove duplicates based on 'id' column

        if end_combined_df is None:
            return df
        else:
            combined_df = pd.concat([df, end_combined_df], ignore_index=True)
            return combined_df[columns_to_keep]
    else:
        return f"Empty response received for location: {location_name}.\n"


def determine_type(value):
    """
    Determines the type of a given value.

    Args:
        value (str): The value to determine the type of.

    Returns:
        str: The determined type ('int64', 'float64', or 'string').
    """
    if value.isdigit():
        return "int64"
    try:
        float(value)
        if "." in value or "e" in value.lower() or "E" in value:
            return "float64"
        elif value.lstrip("-").isdigit():
            return "int64"
        else:
            return "string"
    except ValueError:
        return "string"


def convert_to_type(value, expected_type):
    """
    Converts a value to the expected type.

    Args:
        value (str): The value to convert.
        expected_type (str): The expected type ('int64', 'float64', or 'string').

    Returns:
        The value converted to the expected type.
    """
    if expected_type == "int64":
        return int(value)
    elif expected_type == "float64":
        return float(value)
    else:
        return str(value)


def validate_and_transform_schema(extracted_schema, expected_schema, data_rows):
    """
    Validates and transforms the schema of the extracted data to match the expected schema.

    Args:
        extracted_schema (dict): The schema extracted from the data.
        expected_schema (dict): The expected schema.
        data_rows (list): The data rows to be transformed.

    Raises:
        ValueError: If the schema does not match the expected schema and cannot be transformed.
    """
    for column, expected_dtype in expected_schema.items():
        if column not in extracted_schema:
            logger.error(f"Missing column in extracted data: {column}")
            raise ValueError(f"Missing column in extracted data: {column}")
        if extracted_schema[column] != expected_dtype:
            # Allow int64 to match float64 if expected
            if extracted_schema[column] == "int64" and expected_dtype == "float64":
                for row in data_rows:
                    if row[column] == "":
                        row[column] = None  # or handle as needed
                    else:
                        row[column] = float(row[column])
                extracted_schema[column] = expected_dtype
                continue

            logger.warning(
                f"Data type mismatch for column {column}: expected {expected_dtype}, got {extracted_schema[column]}. Converting to {expected_dtype}."
            )

            # Convert the column values to the expected data type
            for row in data_rows:
                try:
                    if row[column] == "":
                        row[column] = None  # or handle as needed
                    else:
                        row[column] = convert_to_type(row[column], expected_dtype)
                except ValueError as ex:
                    logger.error(
                        f"Failed to convert column {column} to {expected_dtype}: {ex}"
                    )
                    raise ValueError(
                        f"Data type mismatch for column {column}: expected {expected_dtype}, got {extracted_schema[column]}"
                    )

            # Update the extracted schema to reflect the conversion
            extracted_schema[column] = expected_dtype


def validate_and_transform_schema_from_csv(data_text):
    """
    Note: This function is for testing purposes only and therefore has no test coverage.

    Tests the schema of the extracted data against the expected schema and transforms the data if necessary.

    Args:
        data_text (str): The CSV data as a string.

    Returns:
        list: The transformed data as a list of dictionaries.

    Raises:
        ValueError: If the schema does not match the expected schema and cannot be transformed.
    """
    # Load the expected schema from the JSON file
    expected_schema = {
        "time": "string",
        "latitude": "float64",
        "longitude": "float64",
        "depth": "float64",
        "mag": "float64",
        "magType": "string",
        "nst": "float64",
        "gap": "int64",
        "dmin": "float64",
        "rms": "float64",
        "net": "string",
        "id": "string",
        "updated": "string",
        "place": "string",
        "type": "string",
        "horizontalError": "float64",
        "depthError": "float64",
        "magError": "float64",
        "magNst": "int64",
        "status": "string",
        "locationSource": "string",
        "magSource": "string",
    }

    # Parse the CSV data
    csv_reader = csv.reader(StringIO(data_text))
    headers = next(csv_reader)  # Get the headers from the first row

    # Extract the schema from the CSV data
    extracted_schema = {}
    for header in headers:
        extracted_schema[header] = None  # Initialize with None

    data_rows = []
    for row in csv_reader:
        row_dict = {}
        for header, value in zip(headers, row):
            if extracted_schema[header] is None and value:
                extracted_schema[header] = determine_type(value)
            row_dict[header] = value
        data_rows.append(row_dict)

    # Handle columns that remain None (i.e., all values were null)
    for header in headers:
        if extracted_schema[header] is None:
            extracted_schema[header] = "string"  # Default to string for null columns

    # Validate and transform the schema
    validate_and_transform_schema(extracted_schema, expected_schema, data_rows)

    logger.debug("Schema validation and transformation passed.")
    return data_rows
