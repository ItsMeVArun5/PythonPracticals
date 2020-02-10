# W.A.P.P to count the number of characters(character frequency) in a string.

count = 0
element = []

string = "google.com"

for i in string:
    if i not in element:
        element.append(i)
    else:
        continue

    for x in string:
        if i == x:
            count+=1

    element.append(count)
    count = 0
        

print (element)
