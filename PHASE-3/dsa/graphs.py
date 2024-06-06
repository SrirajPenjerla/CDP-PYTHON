def BFS(start,graph):
    visited=[start]
    q=[start]
    while q:
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited

# def DFS(start,graph):
#     ans=[]
#     visited=[start]
#     stack=[start]
#     while stack:
#         ele=stack.pop()
#         ans.append(ele)
#         for i in graph[ele]:
#             if i not in visited:
#                 stack.append(i)
#                 visited.append(i)

#     return visited
def DFS(start,graph,visited=None):
    if not visited:
        visited=[]
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            DFS(i,graph,visited)
    return visited


graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}

# graph={
#     "A":["B","C"],
#     "B":["A","C","D"],
#     "C":["A","B","F"],
#     "D":["B","E"],
#     "E":["D"],
#     "F":["C"]
# }
res1= BFS("D",graph)
print()
res= DFS("D",graph)
print()
print(res1)
print()
print(res)

# ['E', 'C', 'D', 'A', 'B']