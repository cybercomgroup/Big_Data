#!/bin/bash

# Parameters:
# 	MapReduce jar in Local
#	Input path in HDFS
#	Output path in HDFS
#	Weka jar in Local (Optional)

if [ $# -lt 3 ]; then
	echo "Missing required arguments [MapReduce] [Input] [Output]"
	exit 1
fi

if [[ ! -f $1 ]]; then
	echo "MapReduce jar does not exist"
	exit 1
fi

hadoop fs -test -d $2
if [ $? != 0 ]; then
	echo "Input directory does not exist"
	exit 1
fi

now=$(date +"%d-%m-%Y_%H.%M.%S")
outputPath="$3/$now/"

hadoop jar $1 $2 $outputPath

if [ $# -eq 4 ]; then
	hadoop jar $4 "$outputPath/part-m-00000"
fi
