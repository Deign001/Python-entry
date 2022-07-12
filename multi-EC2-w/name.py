#!/usr/bin/env python3

import boto3

AWS_REGION = "us-east-1"
AMI_ID = 'ami-0c02fb55956c7d316' # Amazon Linux 2
SUBNET_ID = 'subnet-0bbad25183268190f'
SECURITY_GROUP_ID = 'sg-03ad58505cf0518a2'
INSTANCE_PROFILE = 'LUIT'

USER_DATA = '''#!/bin/bash
yum update
'''

EC2_RESOURCE = boto3.resource('ec2', region_name='us-east-1b')
EC2_CLIENT = boto3.client('ec2', region_name='us-east-1b')

instances = EC2_RESOURCE.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId=AMI_ID,
    InstanceType='t2.micro',
    SecurityGroupIds=[
        SECURITY_GROUP_ID,
    ],
    SubnetId=SUBNET_ID,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'my-ec2-instance'
                },
            ]
        },
    ]
)

    
for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    
    instance.wait_until_running()
    
    EC2_CLIENT.associate_iam_instance_profile(
        IamInstanceProfile={
            'Name': INSTANCE_PROFILE,
        },
        InstanceId=instance.id,
    )

    print(f'EC2 Instance Profile "{INSTANCE_PROFILE}" has been attached')

    print(f'EC2 instance "{instance.id}" has been started')