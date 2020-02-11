def fact(num):
	fact = 1
	for x in range(1,num+1):
		fact *= x

	return fact

num = int(input("Enter a number: "))
print (fact(num))
