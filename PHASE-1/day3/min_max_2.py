l=[12,42,23,96,7,18,10,133]

# from the list add min value and max value
min=l[0]
max=l[0]
min_in=0
max_in=0
for i in range(len(l)):
    if l[i] >max:
        max=l[i]
        max_in=i
    if l[i]<min:
        min=l[i]
        min_in=i

l[max_in]=max+min
l[min_in]=max-min
print(l)