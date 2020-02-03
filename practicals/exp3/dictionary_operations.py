thisdict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "year" : 1964
}

print ("-------------Accessing item----------------")
print (thisdict["Brand"])
print ()

print ("-------------Changing values----------------")
thisdict["year"] = "2020"
print (thisdict)
print ()

print ("-------------Looping through dictionary----------------")
for x in thisdict:
    print (x)

print ()

print ("-------------Looping through dictionary (keys and values)----------------")
for x,y in thisdict.items():
    print(x, y)

print ()

print ("-------------Dictionary length----------------")
print (len(thisdict))
print ()

print ("-------------Adding item in dictionary----------------")
thisdict["color"] = "red"
print (thisdict)
print ()

print ("-------------Removing item in dictionary----------------")
thisdict.pop("year")
print (thisdict)
print ()

print ("-------------Copy a Dictonary----------------")
copydict = thisdict.copy()
print (copydict)
print ()

print ("-------------Empty a Dictionary----------------")
thisdict.clear()
print (thisdict)
print ()

print ("-------------Nested dictionaries----------------")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print (myfamily)