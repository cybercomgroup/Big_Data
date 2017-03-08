from pyspark import SparkConf
from pyspark import SparkContext
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import random


#To run: PYSPARK_PYTHON=/opt/cloudera/parcels/Anaconda/bin/python spark-submit spark_visualisehottnessbyartist.py /user/cloudera/song/song_final.csv

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

	
def test(row):
	for x in range(0, row.count()):
		if x!=3 and x!=5:
			row[x]=''
	return row

# Init Spark
conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('artisthotness-job')
sc = SparkContext(conf=conf)

rdd = sc.textFile(str(sys.argv[1]))

mapped = rdd.map(lambda line: line.split(',')).map(lambda line: row[3])
mapped2 = rdd.map(lambda line: line.split(',')).map(lambda line: row[5])
maps = mapped.join(mapped2)

df = rddToPand(mapped)
file = open('visualise.txt', 'w')
file.write(str(mapped2.take(10)))
file.close()
