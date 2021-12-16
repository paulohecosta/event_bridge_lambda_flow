import json
import boto3
import os

def lambda_handler(event, context):
    print('lambda_handler example step one')
    client = boto3.client('sns')

    response = client.publish(
        TargetArn=os.getenv('SNS_NAME'),
        Message=json.dumps({"foo": "message in filter"}),
        MessageAttributes={'period': {'DataType': 'String', 'StringValue': 'weekly'}}
    )
    response = client.publish(
        TargetArn=os.getenv('SNS_NAME'),
        Message=json.dumps({"foo": "message out filter"}),
        MessageAttributes={'period': {'DataType': 'String', 'StringValue': 'daily'}}
    )

    client = boto3.client('events')
    response = client.put_events(
        Entries=[ 
            { 
                'Source': 'custom.example', 
                'DetailType': 'transaction', 
                'Detail': '{ "period": "weekly" }', 
                'EventBusName': 'default' 
            },
            { 
                'Source': 'custom.example', 
                'DetailType': 'transaction', 
                'Detail': '{ "period": "daily" }', 
                'EventBusName': 'default' 
            },
        ]
    )

    return {
        'statusCode': 200,
        'message': f'example step one complete'
    }