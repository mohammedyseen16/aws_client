import boto3

import time
# create a client for cloudwatch
client = boto3.client('logs', region_name='us-east-1', aws_access_key_id='',aws_secret_access_key='')


log_group_name = "test-logs"
log_stream_name = "log-stream"
 
# Create or get the log group and log stream
try:
    response = client.create_log_group(logGroupName=log_group_name)
except client.exceptions.ResourceAlreadyExistsException:
    pass

try:
    response = client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
except client.exceptions.ResourceAlreadyExistsException:
    pass

# Get the current timestamp in milliseconds
current_timestamp = int(time.time() * 1000)

# Put log events
log_events = [
    {
        "timestamp": current_timestamp,
        "message": "a new message"
    }
]

response = client.put_log_events(
    logGroupName=log_group_name,
    logStreamName=log_stream_name,
    logEvents=log_events
)

print("Successfully put log events:", response)
