import boto3

#creating an S3 bucket via boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("deignboto3")

response = bucket.create(
    ACL='public-read',
    
    
)

print(response)