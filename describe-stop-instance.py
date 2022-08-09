import boto3

AWS_REGION = 'us-east-1b'
EC2_RESOURCE = boto3.resource('ec2')
INSTANCE_NAME_TAG_VALUE = 'Dev'

instances = EC2_RESOURCE.instances.filter(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'Dev'
            ]
        }
    ]
)

print(f'Instances with Tag "Name={INSTANCE_NAME_TAG_VALUE}":')

for instance in instances:
     try:
          instance.stop()
          print(f'{instance} is stopping... ')
     except:
          print(f'Nothing to stop... ')