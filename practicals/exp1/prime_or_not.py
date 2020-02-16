number = int(input("Enter a number to check prime or not: "))
isprime = False

for x in range(2,number):
	if number%x == 0:
		isprime = False
		break
	else:
		isprime = True

if isprime == True or number == 2:
	print ("its a prime number.")
else:
	print ("its not a prime number.")

