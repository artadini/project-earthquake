import pandas_gbq
from functions.bigquery_client import bigquery_client
from functions.logger import get_logger
import pandas as pd

logger = get_logger("bigquery-functions")


def push_data_to_bigquery(df, project_id, dataset_id, table_name, if_exists="append"):
    """
    Pushes a pandas DataFrame to a BigQuery table.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be pushed.
        project_id (str): The Google Cloud project ID.
        dataset_id (str): The BigQuery dataset ID.
        table_name (str): The name of the BigQuery table.
        if_exists (str, optional): Specifies the behavior when the table already exists.
        Options are 'fail', 'replace', 'append'. Default is 'append'.

    Returns:
        str: A message indicating if the DataFrame was empty.
    """
    df = pd.DataFrame(df)

    # Check if the DataFrame is not empty
    if not df.empty:
        table_id = f"{project_id}.{dataset_id}.{table_name}"
        logger.info(f"Sending data to {table_id}")

        # Create a BigQuery client
        client = bigquery_client()

        # Use the client to push data to BigQuery
        pandas_gbq.to_gbq(
            df,
            table_id,
            project_id=project_id,
            if_exists=if_exists,
            credentials=client._credentials,
        )
    else:
        return "Empty DataFrame received and moving to next location."
