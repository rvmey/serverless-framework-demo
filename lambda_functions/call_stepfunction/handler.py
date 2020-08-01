import json, os, boto3, uuid

sf_client = boto3.client('stepfunctions')

def handler(event, context):
    if os.environ['STAGE'] == 'dev':
        print(json.dumps(event))
    
    region = context.invoked_function_arn.split(":")[3]
    accountId = context.invoked_function_arn.split(":")[4]

    print('queryStringParameters: ' + json.dumps(event['queryStringParameters']))

    action = ""
    if 'action' in event['queryStringParameters']:
        action = event['queryStringParameters']['action']

    sf_input = {
        'foo': 'bar',
        'action': action
    }

    stepfunction_name = str(uuid.uuid4())
    print('stepfunction_name: ' + stepfunction_name)
    
    stateMachineArn = "arn:aws:states:" + region + ":" + accountId + ":stateMachine:" + os.environ['SLS_SERVICE'] + "-" + os.environ['STAGE']

    response = sf_client.start_execution(
        stateMachineArn=stateMachineArn,
        name=stepfunction_name,
        input=json.dumps(sf_input)
    )

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "sf_input": sf_input
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response