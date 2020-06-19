import json
import boto3
import uuid


# define input content
input_content = {
    "TrainingJobName": "BYOCJob-{}".format(uuid.uuid4().hex),
    "ModelName": "BYOCModel-{}".format(uuid.uuid4().hex),
    "EndpointName": "BYOCEndpoint-{}".format(uuid.uuid4().hex)
}


# invoke step function
sfn_client = boto3.client('stepfunctions')
response = sfn_client.start_execution(
    stateMachineArn='arn:aws:states:us-east-1:851108988172:stateMachine:MyBYOC_81d40346065a4d25af4ada500a8c93c7',
    input=str(input_content).replace('\'', '\"')
)
print(response)
print('Done')