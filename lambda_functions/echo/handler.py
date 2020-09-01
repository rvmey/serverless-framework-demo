import json, os, boto3

def hello(event, context):
    if os.environ['STAGE'] == 'dev':
        print('event:')
        print(json.dumps(event))

    if event.get('queryStringParameters'):
        print(json.dumps(event['queryStringParameters']))

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
