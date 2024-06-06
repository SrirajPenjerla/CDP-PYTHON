# a tree is called as selfbalanced or balanced  tree if the absolute diff between left height and the right height should be <=1

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    elif key >=root.data:
        root.right=insert(root.right,key)
    return root

def create_tree(arr):
    root=Node(arr[0])
    for i in range(1,len(arr)):
        insert(root,arr[i])

    return root
from collections import deque
def level_order(root):
    res=[]
    dq=deque()
    dq.append(root)
    while dq:
        r=dq[0]
        res.append(r.data)
        dq.popleft()
        if r.left:
            dq.append(r.left)
        if r.right:
            dq.append(r.right)
    return res

def height(root):
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    if lh>rh:
        return 1+lh
    else:
        return 1+rh

def isbalanced(root):
    if root is None:
        return 0
    isbalanced(root.left)
    isbalanced(root.right)
    lh=height(root.left)
    rh=height(root.right)
    if abs(lh-rh) <= 1:
        return True
    else:
        exit("unbalanced")

def inorder_trav(root):
    res=[]
    if root:
        res=inorder_trav(root.left)
        res.append(root.data)
        res=res+inorder_trav(root.right)

    return res

def lca(a,b,root):
    if a<root.data<b:
        print(root.data)
    elif a<root.data and b<root.data:
        lca(a,b,root.left)
    else:
        lca(a,b,root.right)

root=create_tree([1,2,3,4,5,6])
root2=create_tree([50,30,70,20,40,60,90])
print(inorder_trav(root2))
print(level_order(root2))
if isbalanced(root2):
    print("Balanced")

root3=create_tree([50,30,80,20,40,70,90,10,25,60,85])
print("Least common Ancestor :: ")
lca(60,85,root3)