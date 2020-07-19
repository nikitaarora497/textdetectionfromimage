import csv
import boto3
import os
from flask import Flask, render_template, request

app = Flask(__name__,static_folder = '')

#orignal path of the file
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route("/")
def index():
    return render_template("goto.html")

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket('cloudj2020')
    my_bucket.Object(file.filename).put(Body=file)
    return render_template('complete.html')

@app.route("/files", methods=['POST'])
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket('cloudj2020')
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)

@app.route("/go", methods=['POST'])
def go():
    with open('credentials.csv','r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]

    photo = request.form['fname']

    client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)
    response = client.detect_text(Image ={'S3Object':{'Bucket':'cloudj2020','Name':photo}})
    return render_template("text.html",output = response)

"""
app.route('/tocomp')
def tocomp():
    return render_template("complete.html")
"""

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=80, debug=True)

