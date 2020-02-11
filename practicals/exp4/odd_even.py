def testOddEven(num):
	if num%2 == 0:
		return "its a even number"
	else:
		return "its a odd number"

num = int(input("Enter a number to test: "))
print(testOddEven(num))
