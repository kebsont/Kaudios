# import os
# import boto3
# from botocore.exceptions import NoCredentialsError

# ACCESS_KEY = 'ASIASIZE65TTFYXS6FTQ'
# SECRET_KEY = 'Eb8hp/IFlWC5g57fVhjKD36c31hFuZaLkJDMt+bb'

# """if(os.environ['ACCESS_KEY']):

#     ACCESS_KEY = os.environ['ACCESS_KEY']
#     SECRET_KEY = os.environ['SECRET_KEY']"""
# def upload_to_aws(local_file, bucket, s3_file):
#     s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY)

#     try:
#         s3.upload_file(local_file, bucket, s3_file)
#         print("Upload Successful")
#         return True
#     except FileNotFoundError:
#         print("The file was not found")
#         return False
#     except NoCredentialsError:
#         print("Credentials not available")
#         return False


# uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')
