# Write a Python program to create a tuple and perform  operations on it.

thistuple = ("apple", "cherry", "mango", "orange", "kiwi")

print ("----------------slicing in tuple----------------")
print (thistuple[0:2])
print (thistuple[-4:-1])
print()

print ("----------------changing value in tuple by using constructor----------------")
temp = list(thistuple)
temp[0] = "lemon"
thistuple = list(temp)
print (thistuple)
print()

print ("--------------looping through tuple----------------")
for x in thistuple:
	print(x)

print()


print ("--------------------tuple length---------------------")
print(len(thistuple))
print()

print ("--------------------Add item in tuple----------------")
print("cant add item in tuples")
print()

print ("---------------------deleting tuple-------------------")
print ("del thistuple :-- this will delete the tuple.")
print()

print ("--------------------joining two tuple--------------------")
t1 = (1,3,4)
t2 = (123,12435,1243)

t3 = t1 + t2
print (t3)
print()

