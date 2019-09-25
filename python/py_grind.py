
## Example Python program to download data from an S3 bucket using a timeout via
## the AWS Python API (which seems to be an interface to the C++ API). This code
## was sent to use by AWS Support (Luke Wells <lawells@amazon.com>) and then hacked.
## jhrg 9/19/19

import boto3
import time
from botocore.client import Config
from botocore.exceptions import ReadTimeoutError
import binascii
 
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
bytes='bytes=0-157286400'
# bytes='bytes=0-1024'
# jhrg 9/19/19

# Start the timer
start = time.time()
 
try:
  # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/
  # reference/services/s3.html#S3.Client.get_object
  # 'response['Body'] is an open StreamingBody object
  response = s3.get_object(Bucket='cloudydap', Key=airs_granule, Range=bytes)

except ReadTimeoutError as e:
  print('Error: ' + str(e))

end = time.time()
print("Get object: {}".format(end - start))

one_meg = 1024 * 1024

with open("data.bin", "wb") as ouput:
  while True:
    chunk = response['Body'].read(amt=one_meg)
    if not chunk:
      break
    # ouput.write(binascii.hexlify(chunk))
    ouput.write(chunk)

end = time.time()
print("Total time: {}".format(end - start))
