import boto3

ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIds=['snap-04efc7a3481efef50'])