from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd
import numpy as np

# To run the spark job, run this command:
# PYSPARK_PYTHON=/opt/cloudera/parcels/Anaconda/bin/python spark-submit <file>.py 

# Params: Spark RDD object from a csv-file.
# Returns: Pandas DF of RDD object

def rddToPand(rdd):

	header = "temp"
	first = True
	data = []

	# Convert unicode to ascii
	for x in rdd.collect():
		if first:
			first = False
			header = x.encode("ascii").split(',')
			header[-1] = header[-1].replace('\t', '') # For some reason trackid has a \t in the end. Delete it.

		else:
			t = x.encode("ascii").split(',')
			t[-1] = t[-1].replace('\t', '')
			data.append(tuple(t))

	return pd.DataFrame.from_records(data, columns = header)

# Init Spark
conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('template-job')
sc = SparkContext(conf=conf)


# Read some csv from hdfs
df_full = rddToPand( sc.textFile("hdfs:///user/cloudera/song/song_final.csv") )

df_loc = df_full[ df_full["Song_Hottness"] != ""]
df_hdfs = df_full[ df_full["Song_Hottness"] == ""]

df_loc.to_csv("song_train.csv", index = False)
df_hdfs.to_csv("song_test.csv", index = False)



