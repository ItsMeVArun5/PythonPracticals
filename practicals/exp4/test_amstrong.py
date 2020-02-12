def testAmstrong(num):
	sum = 0
	for x in str(num):
		sum +=int(x)**3

	if sum == num:
		return "its a amstrong number."

	return "its not a amstrong number."

num = int(input("Enter a number to test amstrong: "))
print (testAmstrong(num))
