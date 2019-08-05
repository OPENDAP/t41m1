#!/bin/bash
#
# Usage: time2csv <file> > <output file>

echo "# Source $1"

# Assume the data in the text file is output from `time -p`
awk 'BEGIN {print "real, user, sys"}
/real/ {real=$2}
/user/ {user=$2}
/sys/ {printf "%s, %s, %s\n", real, user, $2}' $1


