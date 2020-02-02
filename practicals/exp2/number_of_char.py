# W.A.P.P to count the number of characters(character frequency) in a string.

string = "google.com"
freq = {}

for i in string:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1

print (freq)
