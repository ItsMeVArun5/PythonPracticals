# W.A.P.P to create a set and perform following operations on it: a]iteration over sets. b]to add members in a set. c]To remove items from set. d]To remove an item from a set if it is present in a set. e]To create an intersection of sets.

names = {"varun", "pranali", "ashutosh", "chaitanya"} 

# a] Iteration over set...........................
for x in names:
	print (x)

# b] Add members in a set......................
names.add("priyal")
print (names)

# c] Remove an item...................
names.remove("varun")
print (names)

# d] Remove an item if it is present..............
if "pranali" in names:
	names.remove("pranali")

print (names)

# e] intersection of sets...............
name = {"ashutosh", "chaitanya", "varun", "harsh"}
intersec = names.intersection(name)
print (intersec)
