
## Example python program to download data from an S3 bucket using a timeout via
## the AWS Python API (which seems to be an interface to the C++ API). This code
## was sent to use by AWS support (Luke Wells <lawells@amazon.com>). jhrg 9/19/19

import boto3
import time
from botocore.client import Config
from botocore.exceptions import ReadTimeoutError
 
# timeout value; was initially 0.05 but that was always giving a timeout error.
# jhrg 9/19/19
timeout=0.5

# Initialize S3 client config with read_timeout set to an arbitrarily low number
config = Config(connect_timeout=5, read_timeout=timeout, retries={'max_attempts': 0})
s3 = boto3.client('s3', config=config)
 
# Try to download the byte range (150MB)
# Bucket is 'cloudydap'

# S3 Object key is an AIRS Granule
airs_granule='airs/AIRS.2015.01.01.L3.RetStd_IR001.v6.0.11.0.G15013155825.nc.h5'
bytes='0-157286400'
# jhrg 9/19/19

# Start the timer
start = time.time()
 
try:
  s3.get_object(Bucket='cloudydap', Key=airs_granule, Range=bytes)
# Catch my ReadTimeoutError
except ReadTimeoutError as e:
  # Stop the timer and print to screen
  print('Error: ' + str(e))

end = time.time()
print(end - start)
