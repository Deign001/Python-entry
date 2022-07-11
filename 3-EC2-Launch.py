import boto3
KeyName = "launchtime"

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-0cff7528ff583bf9a',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        KeyName=KeyName,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Production'},
                {'Key': 'Env','Value': 'Production'}]
                          },
                      ]),
ec2_resource.create_instances(ImageId='ami-0cff7528ff583bf9a',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        KeyName=KeyName,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Security'},
                {'Key': 'Env','Value': 'Security'}]
                          },
                      ]),
ec2_resource.create_instances(ImageId='ami-0cff7528ff583bf9a',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        KeyName=KeyName,
        TagSpecifications=[
            {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name','Value': 'Dev'},
                    {'Key': 'Env','Value': 'Dev'}]
                                },
                        ])
                        