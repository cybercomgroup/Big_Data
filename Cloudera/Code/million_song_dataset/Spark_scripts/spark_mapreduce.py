from pyspark import SparkConf
from pyspark import SparkContext
import pandas as pd

#To run: PYSPARK_PYTHON=/opt/cloudera/parcels/Anaconda/bin/python spark-submit spark_mapreduce.py

def rddToPand(RDD):

	header = "temp"
	first = True
	data = []

	# Convert unicode to ascii
	for x in RDD.collect():
		if first:
			first = False
			header = x.encode("ascii").split(',')

		else:
			data.append(tuple(x.encode("ascii").split(',')))

	return pd.DataFrame.from_records(data, columns = header)
		

def replace_line(line, toreplace, replacewith):
	if line==toreplace:
		return replacewith
	else:
		return line

def replace_row(row, toreplace, replacewith):
	if row[0]==toreplace:
		row[0]=replacewith
		return row
	else:
		return row

# Init Spark
conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('mapreduce-job')
sc = SparkContext(conf=conf)

# Read some csv from hdfs
rdd = sc.textFile("hdfs:///user/cloudera/song/test.csv")

##### MAP FUNCTIONS
#Replaces a line then split into rows
mapped = rdd.map(lambda line: replace_line(line, '0,"hej",4,0', 'IT WORKED')).map(lambda line: line.split('\t'))
file = open('output2.txt', 'w')
file.write(str(mapped.take(5)))
file.close()

#Split into rows then replace a value in a row.
omapped = rdd.map(lambda line: line.split('\t')).map(lambda row: replace_row(row, '0,"hej",4,0', 'IT WORKED')).map(lambda row: replace_row(row, 'ID,Text,Heltal,Extra', 'IT WORKED'))
file = open('output3.txt', 'w')
file.write(str(omapped.take(5)))
file.close()

##### REDUCE FUNCTIONS
#Count all occurances of identical first values in rows
reduced = omapped.map(lambda row: (row[0], 1)).reduceByKey(lambda x, y: x+y)
file = open('output4.txt', 'w')
file.write(str(reduced.take(5)))
file.close()

# Parse rdd to pandas object
#df = rddToPand(rdd)


