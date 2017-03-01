from pyspark import SparkConf
from pyspark import SparkContext
import pandas as pd

# To run the spark job, run this command:
# PYSPARK_PYTHON=/opt/cloudera/parcels/Anaconda/bin/python spark-submit <file>.py 

# Params: Spark RDD object from a csv-file.
# Returns: Pandas DF of RDD object
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

# Init Spark
conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('template-job')
sc = SparkContext(conf=conf)

# Read some csv from hdfs
rdd = sc.textFile("hdfs:///user/cloudera/song/test.csv")

# Parse rdd to pandas object
df = rddToPand(rdd)

# Do what you want with the pandas dataframe
file = open('output.txt', 'w')
file.write(str(df.describe()))
file.write("\n\n-------------------------\n\n")
file.write(str(df.head()))

