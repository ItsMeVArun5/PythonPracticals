#  Write a Python program to convert and display decimal to binary equivalent.

num = int(input("Enter decimal number: "))

binary_num = ""

while num>=1:
	if num%2 == 0:
		binary_num += str("0")
	else:
		binary_num += str("1")
	
	num = num/2


print (binary_num[::-1])
