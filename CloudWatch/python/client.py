import boto3

import time
# create a client for cloudwatch
client = boto3.client('logs', region_name='us-east-1', aws_access_key_id='',aws_secret_access_key='')
log_group = "test-logs"
log_stream = "log-stream"

try:
    response = client.create_log_group(logGroupName=log_group)
except client.exceptions.ResourceAlreadyExistsException:
    pass
try:
    response = client.create_log_stream(logGroupName=log_group,logStreamName=log_stream)
except client.exceptions.ResourceAlreadyExistsException:
    pass


response = client.put_log_events(
    logGroupName=log_group,
    logStreamName=log_stream,
    logEvents=[
        {"timestamp": int(time.time() * 1000), "message": "hello im yaseen"},
    ],
)
print(response)
