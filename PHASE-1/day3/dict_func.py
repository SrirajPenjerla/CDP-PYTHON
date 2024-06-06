# creation of dict with 4 key value pairs

mydict={1:"loki",
        2:"harsha",
        "3":"filtr",
        3:34,
        4:"nan",
        5:"loki"}
print(mydict)

# accessing your values using keys
print(mydict[1])
print(mydict["3"])
print(mydict[4])

# accesing the whole dict using for loops 

for key in mydict:
    print(key ,mydict[key])

#try to change in exisiting vakue mutability
    
mydict[4]="Lokiii"
print(mydict[4])