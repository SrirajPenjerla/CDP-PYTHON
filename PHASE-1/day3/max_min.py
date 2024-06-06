
l=[12,42,23,96,7,18,10,133]

count=0
for i in l:
    count+=1
# from the list add min value and max value
min=l[0]
max=l[0]
lo=0
s=0

for i in range(count):
    if l[i] >max:
        max=l[i]
        lo=i
    if l[i]<min:
        min=l[i]
        s=i

l[lo]=max+min
l[s]=max-min

    
print(l)
