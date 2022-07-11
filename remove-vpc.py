import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId='string', #paste your VPC Id for "string"
    DryRun=True/False
    )