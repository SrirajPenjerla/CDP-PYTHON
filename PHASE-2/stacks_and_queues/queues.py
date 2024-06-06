from collections import deque

dq1=deque()
s=[]

dq1.append(1)
dq1.append(2)
dq1.append(3)
dq1.append(4)
dq1.append(5)
dq1.append(6)

# for i in range(len(dq1)):
#     s.append(dq1.popleft())

# for i in range(len(s)):
#     dq1.append(s.pop())


print(dq1)

# def reeev(n):
#     for i in range(n):
#         s.append(dq1.popleft())
#     for i in range(len(s)):
#         dq1.append(s.pop())

#     print(dq1)

n=3
for i in range(n):
    ele=dq1.popleft()
    s.append(ele)

while(len(s)!=0):
    dq1.append(s.pop())
    
for i in range(len(dq1)-n):
    dq1.append(dq1.popleft())

print(dq1)
