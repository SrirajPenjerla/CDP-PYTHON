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

def inorder_trav(root):
    res=[]
    if root:
        res=inorder_trav(root.left)
        res.append(root.data)
        res=res+inorder_trav(root.right)

    return res

def preorder_trav(root):
    res=[]
    if root:
        res.append(root.data)
        res=res+preorder_trav(root.left)
        res=res+preorder_trav(root.right)
    return res

def postorder_trav(root):
    res=[]
    if root:
        
        res=res+postorder_trav(root.left)
        res=res+postorder_trav(root.right)
        res.append(root.data)
    return res

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


def right_view(root):
    # res=[]
    if root.right is None:
        return
    print(root.right.data)
    right_view(root.right)

def top_view(root):
    l1=trav_lef(root.left)
    l2=trav_rig(root.right)
    l1.append(root.data)
    return l1+l2

def trav_lef(root):
    lis=[]
    if root.left is None:
        return lis
    lis.append(root.data)
    lis=lis+trav_lef(root.left)
    return lis

def trav_rig(root):
    if root is None:
        return
    lis=[]
    lis.append(root.data)
    lis=lis+trav_rig(root.right)
    return lis


def height(root):
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    if lh>rh:
        return 1+lh
    else:
        return 1+rh

def create_bst(arr):
    root=Node(arr[0])
    for i in range(1,len(arr)):
        insert(root,arr[i])

    return root

root=create_bst([50,30,70,20,40,60,90])

print("Inorder :: ",inorder_trav(root))
# print(root.data)
print("Pre Order :: ",preorder_trav(root))

print("Post Order :: ",postorder_trav(root))

print("Level Order :: ",level_order(root))

print("Height of tree :: ",height(root))

right_view(root)

print(top_view(root))