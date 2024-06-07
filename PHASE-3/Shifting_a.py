n=input().lower()
print(n)
stack=[-1]
count=0
for i in n:
    if stack[-1] == -1:
        stack.append(i)
    else:
        if stack[-1] != i:
            count+=1
            stack.append(i)

print(stack)
print(count)
