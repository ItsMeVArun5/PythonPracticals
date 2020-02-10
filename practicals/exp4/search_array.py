# Write a Python Program to search an element in array and display its location (Create Definition searchInArray(element,array).


def searchArray(element, array):
	pos = 0
	index = 0
	found = False
	for x in array:
		index += 1
		if element == x:
			found = True
			pos = index

	if found == True:
		print ("location found and its position is:", pos)
	else:
		print ("Not Found")


array = [1,4,5,3,25]
element = int(input("Enter the element to search: "))
searchArray(element, array)
