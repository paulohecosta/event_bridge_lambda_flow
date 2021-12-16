import json

def lambda_handler(event, context):
    print('lambda_handler example step two')
    return {
        statusCode: 200,
        message: f'example step two complete'
    }