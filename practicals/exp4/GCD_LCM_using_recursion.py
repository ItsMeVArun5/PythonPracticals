# GCD and LCM using recursion.

def gcd(x, y):
	if (y == 0):
		return x
	else:
		return gcd(y, x%y)

result = gcd(12, 24)
print (result)

def lcm(x, y, counter=1):
	if counter%x==0 and counter%y==0:
		return counter
	else:
		return lcm(x, y, counter+1)

print (lcm(4, 5))
