# Write a Python program to Print all factors of number and print if the no is perfect number.

num = int(input("Enter a number: "))
factors = []

for x in range(1,num):
	if num%x == 0:
		factors.append(x)

print ("factors are:", factors)
if sum(factors) == num:
	print ("number:", num, "is a perfect number.")
