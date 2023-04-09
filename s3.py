import boto3
s3 = boto3.client('s3')
bucket_name = 'my-wallpaper1-bucket'

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2' # Replace with your desired region
    }
)

print(response)

import boto3
client = boto3.client('rds')

response = client.create_db_instance(
        AllocatedStorage=10,
        DBName="test",
        DBInstanceIdentifier="my-first-rds-instance",
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername="root",
        MasterUserPassword="pass1234",
        Port=3306
)

print (response)