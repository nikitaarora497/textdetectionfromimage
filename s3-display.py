import csv
import boto3
import os
from flask import Flask, render_template, request

app = Flask(__name__,static_folder = '')

@app.route('/')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket('flaskbucket')
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)


if __name__ == "__main__":
    app.run(port=5005, debug=True)