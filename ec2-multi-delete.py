import boto3

ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()

x.keys()

data=x["Reservations"]

li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
        
#This last part will terminate instances, so I am commenting it out so that it will not be done on accident
#ec2_client.terminate_instances(InstanceIds=li)

