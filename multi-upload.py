#upload multiple files
import boto3 
cwd=os.getcwd()
#cwd=cwd+"/boto3_tutorial/" noted out because cwd did not require additonal folders added
files=glob.glob(cwd+"/*.txt")

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="totaltech",
    Key=file.split("/")[-1])

print(cwd)    
print(files)   