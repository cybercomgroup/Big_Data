import pydoop.hdfs as hdfs

hdfs.mkdir("test")
hdfs.dump("hello hadoop", "test/hello.txt")

text = hdfs.load("test/hello.txt")
print(text)
