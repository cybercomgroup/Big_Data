def mapper (_, text, writer)
	for word in text.split():
		writer.emit(word, "1")

def reducer (word, icounts, writer):
	print("word: "+str(word))
	print("sum: "+str(sum(map(int, icounts)))
	writer.emit(word, sum(map(int, icounts)))
