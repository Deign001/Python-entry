import boto3

ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1b',
    Encrypted=True,
    Size=12,
    SnapshotId="snap-04efc7a3481efef50",
    VolumeType="gp2")