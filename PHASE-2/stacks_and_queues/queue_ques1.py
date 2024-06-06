#input=list[-8,2,3,-6,10]#
#for every window of 2 ele return the first neg number window =2 when no neg num ans should be 0 using queues 
#only use popleft() and append()
from collections import deque
l=[-8,2,3,-6,10]
l=[-4,-2,3,-5,-6,1]
dq=deque()
k=2
for i in range(k):
    if l[i]<0:
        dq.append(i)

for i in range(k,len(l)):
    if not dq:
        print(0)
    else:
        print(l[dq[0]])
    while(dq and i-dq[0]>=k):
        dq.popleft()

    if (l[i]<0):
        dq.append(i)

if len(dq)>0:
    print(l[dq[0]])
else:
    print(0)

