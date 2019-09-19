
## Example python program to download data from an S3 bucket using a timeout via
## the AWS Python API (which seems to be an interface to the C++ API). This code
## was sent to use by AWS support (Luke Wells <lawells@amazon.com>). jhrg 9/19/19

import boto3
import time
from botocore.client import Config
from botocore.exceptions import ReadTimeoutError
 
 
# Initialize S3 client config with read_timeout set to an arbitrarily low number
config = Config(connect_timeout=5, read_timeout=.05, retries={'max_attempts': 0})
s3 = boto3.client('s3', config=config)
 
# Start the timer
start = time.time()
 
# Try to download the byte range (150MB)
# Bucket is 'cloudydap'
# Key is 'AKIAIQP3EXFOCKTROGXQ' which is my (jimg) key. I have my private key in 
# for that public set in the .aws/credentials file. jhrg 9/19/19
try:
  s3.get_object(Bucket='cloudydap', Key='AKIAIQP3EXFOCKTROGXQ', Range='bytes=0-157286400')
# Catch my ReadTimeoutError
except ReadTimeoutError as e:
  # Stop the timer and print to screen
  end = time.time()
  print(end - start)
