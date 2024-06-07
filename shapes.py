shapes=[]
n=[[0,3,4],[0,2,5],[1,2,3],[1,5,2],[0,2,4],[1,2,2]]
ans=[]

for i in range(len(n)):
    if n[i][0] == 0:
        shapes.append(n[i])
    else:
        count=0
        for j in range (len(shapes)):
            if n[i][1] <= shapes[j][1] and n[i][2] <= shapes[j][2] or  n[i][2]<= shapes[j][1] and n[i][1] <= shapes[j][2] :
                count+=1
        if count == len(shapes):
            ans.append(True)
        else:
            ans.append(False)

print(ans)