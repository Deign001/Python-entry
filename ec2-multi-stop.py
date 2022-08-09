import boto3

ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()

x.keys()

data=x["Reservations"]

departments=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        departments.append(instance_id)
        
ec2_client.stop_instances(InstanceIds=departments)

