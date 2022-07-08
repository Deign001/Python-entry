import boto3
#how to upload multiple files
import os
import glob

s3_resource=boto3.client("s3")

s3_resource.upload_file(
    #Filename="yourfilenamehere",
    #Bucket="yourbucketnamehere",
    #Key="yourkeyhere")

cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"/*.png")

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
   # Bucket="yourbucketnamehere",
    Key=file.split("/")[-1]) #-1 identifies the final object

print(cwd)    
print(files)   
