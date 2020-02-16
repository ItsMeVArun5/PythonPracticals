number = int(input("Enter a number to find its factorial: "))
fact = 1

for x in range(1,number+1):
	fact = fact * x

print (fact)
