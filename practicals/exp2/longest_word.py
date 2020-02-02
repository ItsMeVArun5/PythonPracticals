# W.A Python function that takes a list of words and return the length of the longest one.

word_list = ["varun", "there", "list", "word", "longest"]

def longestWord(list):
	length_list = []
	for x in list:
		length_list.append(len(x))

	print ("longest word:" + str(max(length_list)))


longestWord(word_list)
