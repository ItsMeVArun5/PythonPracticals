# GCD using recursion.

def gcd(x, y):
	if (y == 0):
		return x
	else:
		return gcd(y,x%y)

result = gcd(12, 24)
print (result)
