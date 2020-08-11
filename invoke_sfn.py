import json
import uuid
import boto3


# define input content
input_content = {
    "TrainingJobName": "BYOCJob-{}".format(uuid.uuid4().hex),
    "ModelName": "BYOCModel-{}".format(uuid.uuid4().hex),
    "EndpointName": "BYOCEndpoint-{}".format(uuid.uuid4().hex)
}


# invoke step function
sfn_client = boto3.client('stepfunctions')
response = sfn_client.start_execution(
    stateMachineArn='arn:aws:states:us-east-1:your_account_id:stateMachine:your_step_functions_name',
    input=str(input_content).replace('\'', '\"')
)
print(response)
print('Done')
