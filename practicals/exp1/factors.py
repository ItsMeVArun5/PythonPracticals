number = int(input("Enter the number to find its factors: "))
print ("factors are: ")

for x in range(1,number+1):
	if number%x == 0:
		print(x)
