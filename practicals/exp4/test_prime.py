def testPrime(num):
	for x in range(2,num):
		if num%x == 0:
			return "its not a prime number"
			break

	return "its a prime number"

num = int(input("Enter a number to test prime: "))
print (testPrime(num))
