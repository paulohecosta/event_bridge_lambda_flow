import json
import boto3
import os

def lambda_handler(event, context):
    print('lambda_handler example step one')
    message = {"foo": "bar"}
    
    client = boto3.client('sns')

    response = client.publish(
        TargetArn=os.getenv('SNS_NAME'),
        Message=json.dumps(message),
        MessageAttributes={'period': {'DataType': 'String', 'StringValue': 'weekly'}}
    )
    response = client.publish(
        TargetArn=os.getenv('SNS_NAME'),
        Message=json.dumps(message),
        MessageAttributes={'period': {'DataType': 'String', 'StringValue': 'daily'}}
    )

    return {
        'statusCode': 200,
        'message': f'example step one complete'
    }