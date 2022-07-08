import boto3
s3_resource=boto3.client("s3")

#delete single object
objects=(s3_resource.delete_objects(Bucket="YOURBUCKETNAMEHERE"))["OBJECTNAMEHERE"]

#delete multiple objects
import os
import glob

s3_resource.list_objects(Bucket="YOURBUCKETNAMEHERE"))["Contents"]

len(objects)

#iteration
for object in objects:
    print(object["key]"])
    s3_resource.delete_objects(Bucket="YOURBUCKETNAMEHERE", Key=object["Key"])
