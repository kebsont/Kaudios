"""
for f in rest:
    print(f)
    with s3_client.open(f, 'r') as fu:
        ftp.storbinary('STOR ' + posixpath.basename(f), fu)
"""


import boto3

ACCESS_KEY = 'ASIASIZE65TTFYXS6FTQ'
SECRET_KEY = 'Eb8hp/IFlWC5g57fVhjKD36c31hFuZaLkJDMt+bb'
s3 = boto3.client('s3',aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
# s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
with open('02_HOUBA_18_SAFAR_Kourel_1_Touba_Bichri.mp3', 'wb') as f:
    s3.download_fileobj('khassida-audio', 'media/', f)
