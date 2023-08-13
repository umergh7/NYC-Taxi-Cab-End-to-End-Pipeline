import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from io import BytesIO
import boto3


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    s3 = boto3.client('s3')

    # Replace 'your-bucket-name' and 'your-file-path' with the actual S3 bucket and file path.
    bucket_name = 'nyc-taxidata-bucket'
    file_path = 'uber_data.csv'

    # Define the S3 object key using the file path
    s3_object_key = file_path

    # Use 'get_object' to retrieve the CSV file from S3
    response = s3.get_object(Bucket=bucket_name, Key=s3_object_key)

    df = pd.read_csv(response['Body'])

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
