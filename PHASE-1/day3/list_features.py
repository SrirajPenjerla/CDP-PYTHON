#creation of list
lis=[1,"loki",30.5,"harsha",4,55,0]

#acessing elements
print(lis[0]) 
print(lis[5])

#slicing
print(lis[1:3])
print(lis[::-1])
print(lis[:4])
print(lis[2:])

#loops accesing
for l in lis:
    print(l,end=" ")

i=0
while(i<len(lis)):
    print(lis[i],end=" ")
    i=i+1

#append
print()
lis.append("hello World")
print(lis)

#insert
lis.insert(9,23)
print()
print(lis)

#multi dim lists
lis2d=[[1,2],["a","b"]]
print(lis2d[0][0])
print(lis2d)

#updating values 

lis[1]="hell"
print(lis)