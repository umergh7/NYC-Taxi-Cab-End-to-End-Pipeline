from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from pandas import DataFrame
from os import path
from io import StringIO
import boto3


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a S3 bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#s3
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'nyc-taxidata-output'
    object_key = 'fact_table/fact_table.csv'


    s3 = boto3.client('s3')

    # Replace 'your-bucket-name' and 'your-file-path' with the actual S3 bucket and file path.
    bucket_name = 'nyc-taxidata-output'
    file_path = '/home/ec2-user/nyctaxi/tmp/fact_table.csv'

    df.to_csv(file_path, index=False)
    # s3.upload_file('jobs.csv', bucket, folder+'jobs.csv')
    s3.upload_file(file_path, bucket_name, 'fact_table/fact_table.csv')
