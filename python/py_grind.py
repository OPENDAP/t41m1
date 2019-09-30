
## Example Python program to download data from an S3 bucket using a timeout via
## the AWS Python API (which seems to be an interface to the C++ API). This code
## was sent to use by AWS Support (Luke Wells <lawells@amazon.com>) and then hacked.
## jhrg 9/19/19

import boto3
import time
import sys
from botocore.client import Config
from botocore.exceptions import ReadTimeoutError
 
def read_bytes(airs_granule):
  """Use the boto3 s3 API to build a response object for a range-get 
  read from an object in a S3 bucket. Then read those data and dump
  them in a temporary file. Compute and print the time to build the
  response object and get the data for later analysis.

  If the read operation fails to complete, return False, otehrwise
  return True."""

  # Bucket is 'cloudydap'

  # S3 Object key is an AIRS Granule
  object='airs/' + airs_granule

  # Try to download the byte range (150MB)
  bytes='bytes=0-157286400'
  # bytes='bytes=0-1024'
  # jhrg 9/19/19

  # Start the timer
  start = time.time()
  status = True

  try:
    # Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/
    # reference/services/s3.html#S3.Client.get_object
    # 'response['Body'] is an open StreamingBody object
    response = s3.get_object(Bucket='cloudydap', Key=object, Range=bytes)
    end = time.time()
    print("Get object, {}".format(end - start))

    with open("data.bin", "wb") as ouput:
      while True:
        chunk = response['Body'].read(amt=one_meg)
        if not chunk:
          break
        ouput.write(chunk)

  except ReadTimeoutError as e:
    print('Error: ' + str(e))
    status = False

  end = time.time()
  print("Time, {}".format(end - start))

  return status

##
## Main
##

arguments = len(sys.argv) - 1
if arguments == 0:
  print("Usage {}: timeout value [object names]".format(sys.argv[0]))
  exit(1)

# timeout value; was initially 0.05 but that was always giving a timeout error.
# jhrg 9/19/19
timeout = float(sys.argv[1])

if (arguments == 2):
  filepath = sys.argv[2]
else:
  filepath = '../airs_AggFiles'

with open(filepath) as fp:
  line = fp.readline()
  cnt = 1

  # Initialize S3 client config with read_timeout set to an arbitrarily low number
  config = Config(connect_timeout=5, read_timeout=timeout, retries={'max_attempts': 0})
  s3 = boto3.client('s3', config=config)

  one_meg = 1024 * 1024

  while line:
    print("{}, {}".format(cnt, line.strip()))
    
    start = time.time()
    trial = 1
    print("Trial: {}".format(trial))
    status = read_bytes(line.strip())

    while not status:
      trial += 1
      print("Trial: {}".format(trial))
      status = read_bytes(line.strip())

    print("Total Time, {}".format(time.time() - start))
    sys.stdout.flush()

    line = fp.readline()
    cnt += 1
