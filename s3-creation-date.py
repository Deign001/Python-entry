import boto3
#print any variable by ID

s3_resource=boto3.client("s3")

#Identify the bucket in the list using an integer
s3_name=s3_resource.list_buckets()["Buckets"][1]["Name"]

#print out the creation date of the 1st bucket
creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"] 

#Creation date of the 5th bucket
creation_date1=creation_date.strftime("%d%m%y_%H:%M:%s") #Day, Month, Year - Hour:Min:Second

#print out dictionary of buckets w/ name, creation date
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket)

#print the name of bucket and the creation date   
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])