import os
import json
from ftplib import FTP
import boto3

# Source https://github.com/Vibish/FTP_SFTP_LAMBDA/blob/master/FTPThroughLambda.py
# https://www.edureka.co/community/17558/python-aws-boto3-how-do-i-read-files-from-s3-bucket
# https://medium.com/better-programming/transfer-file-from-ftp-server-to-a-s3-bucket-using-python-7f9e51f44e35
# https://github.com/kirankumbhar/File-Transfer-FTP-to-S3-Python/blob/master/ftp_to_s3.py
# https://dashbird.io/blog/python-aws-lambda-error-handling/

# For example: FTP_HOST = ftp.your_ftp_host.com
FTP_HOST = 'ftp.daarayislam.com'
FTP_USER = 'daara1365613'
FTP_PWD = 'F8V8H3X2C5k6'
# For example: FTP_PATH = '/home/logs/'
FTP_PATH = '/home/logs'


s3_client = boto3.client('s3')

def handler(event, context):

    if event and event['Records']:
        for record in event['Records']:
            sourcebucket = record['s3']['bucket']['name']
            sourcekey = record['s3']['object']['key']
            
            #Download the file to /tmp/ folder
            filename = os.path.basename(sourcekey)
            download_path = '/tmp/'+ filename
            print(download_path)
            s3_client.download_file(sourcebucket, sourcekey, download_path)
            
            os.chdir("/tmp/")
            with FTP(FTP_HOST, FTP_USER, FTP_PWD) as ftp, open(filename, 'rb') as file:
                ftp.storbinary('{FTP_PATH}{file.name}', file)

            #We don't need the file in /tmp/ folder anymore
            print(filename)
            os.remove(filename)
