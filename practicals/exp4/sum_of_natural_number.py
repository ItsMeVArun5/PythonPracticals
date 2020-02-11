def sumN(num):
	sum = 0
	for x in range(1,num+1):
		sum += x

	return sum


num = int(input("Enter a N number: "))
print (sumN(num))

