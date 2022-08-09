#Boto3 is the AWS - Software Development Kit (SDK) - for Python
# This allows Python developers to write software that makes use of AWS services.
import boto3

#Identify the service resource.
sqs = boto3.resource('sqs') 

# Create the queue.
queue = sqs.create_queue(QueueName='Best-Q-Ever')

# Access identifiers
print(queue.url)

#for more info, https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html