# aws_bes_test
The bash script `aws_bes_test` can be run to utilize hyrax, besstandalone, and 
curl to time the retrieval of data from S3.


## Test Datasets
The test datasets are a set of 365 level 3 AIRS datasets which are available in 
the S3 bucket `cloudydap`. This collection of AIRS datasets represents a year of 
data product and they can be aggregated using the **joinNew** method. Each of
these datasets have been examined and their internal structural information 
stored in dmr++ format.  
 
The dmr++ _dataset_ files each represent a single hdf5 file in S3 and contain 
a map of each variables chunk locations. 
 
The dmr++ _aggregation_ files contain aggregated variables which are defined by 
the union of the chunk maps of their constituent members. 

## Tests
This script runs 5 tests, each described below. In each of these tests a "rep" 
is a set of one or more activities the result of which is acquiring all of the
data for the aggregated variable ```ClrOLR_A```. In other words, each "rep" 
retrieves just the data for the variable ```ClrOLR_A``` from each of the 365 
hdf5 objects in the S3 bucket ```cloudydap```.


1. `bess_airs_dmrpp_datasets` - This test utilizes `besstandalone` requests to 
retrieve the ClrOLR_A variable from each of the 365 dmr++ datasets for the 
aggregated AIRS virtual dataset. Each "rep" represents the same number of S3 
accesses as requesting the aggregated ClrOLR_A from an NcML aggregation or from 
a dmr++ aggregation.

1. `bess_airs_onevar_dmrpp_agg` - The test utilizes a single `besstandalone` 
request to retieve the entire (365 aggregated time points) data value for the 
ClrOLR_A variable from the dmr++ aggregation `dmrpp_agg_test_06.dmrpp`. Each 
pass/rep/count values represents a single request for the aggregated ClrOLR_A 
value which will have the same number of S3 accesses as the same request put to 
the NcML aggregation of dmr++ file and as each "rep" in the first test, 
`bess_airs_dmrpp_datasets`. 

1. `curl_range_get_airs_onevar_chunks` - This test utilizes command line `curl` 
and its range GET capability to retreive each chunk of the 365 file aggregated 
variable ClrOLR_A from the various hdf5 objects held in S3. Each "rep" retrieves 
the value of the aggregated variable.

1. `hyrax_airs_dmrpp_dataset_files` - This test utilizes command line `curl` to 
GET the ClrOLR_A variable data response for each of the 365 dmr++ files in the 
AIRS aggregation. Again this is the same number of S3 accesses as previous 
tests.

1. `hyrax_airs_onevar_dmrpp_agg` - This test utilizes command line `curl` to GET 
the aggregated ClrOLR_A variable data response from dmr++ aggregation, 
`dmrpp_agg_test_06.dmrpp`. Each "rep" gets the full value of the aggregated 
variable and again, makes the same number of S3 access as the other tests.
