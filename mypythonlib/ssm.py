import os
import boto3
import botocore.exceptions

def get_parameters(param_key: str, region_name: str):
    ssm = boto3.client('ssm', region_name)
    response = ssm.get_parameters(
        Names=[
            (param_key),
        ],
        WithDecryption=True
    )
    return response['Parameters'][0]['Value']