import csv
import boto3

with open('credentials.csv','r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = '1.png'

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)
response = client.detect_text(Image ={'S3Object':{'Bucket':'flaskbucket','Name':photo}})

print(response)
      
        
