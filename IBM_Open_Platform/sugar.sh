#!/bin/bash

# Parameters:
# 	MapReduce jar in Local
#	Input path in HDFS
#	Output path in HDFS
#	Weka jar in Local (Optional)

if [ $# -lt 3 ]; then
	echo "Missing required arguments [MapReduce] [Input] [Output]"
	exit
fi

if [[ ! -f $1 ]]; then
	echo "MapReduce jar does not exist"
	exit
fi

if [ hadoop fs -test -d $2 != 0 ]; then
	echo "Input directory does not exist
	exit
fi

now = date + "%d-%m-%y_%H:%M:%S"
outputPath = "$3/$now"

hadoop jar $1 $2 $outputPath

if [ $# -eq 4 ]; then
	java jar $4 "$outputPath/part-m-00000"
fi
