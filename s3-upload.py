import boto3

s3 = boto3.client('s3')
s3.upload_file('D:/vit stuff/sem 2/Cloud J component/image1.jpg','flask-mybucket','first.jpg')

print("upload done")
