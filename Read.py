entry = []
with open("Test.txt","r") as t:
    for i in t:
        x = i.strip()
        entry.append(x)

e1 = entry[0]        
e2 = entry[1]
e3 = entry[2]
print (e1)
print (e2)
print (e3)