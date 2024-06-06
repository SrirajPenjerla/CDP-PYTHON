class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(50)
new=Node(30)
root.left=new
new=Node(70)
root.right=new
new=Node(20)
root.left.left=new
new=Node(40)
root.left.right=new
# temp=root
# left=None
# right=None
# while temp.right and temp.left !=None:
#     print(left)
#     print(right)
#     right=root.right.data
#     left=root.left.data
def inorder_trav(root):
    res=[]
    if root:
        res=inorder_trav(root.left)
        res.append(root.data)
        res=res+inorder_trav(root.right)

    return res

def inorder_trav(root):
    # res=[]
    if root is None:
        return
    inorder_trav(root.left)
    print(root.data)
    inorder_trav(root.right)

def preorder_trav(root):
    # res=[]
    if root is None:
        return
    print(root.data)
    preorder_trav(root.left)
    preorder_trav(root.right)
        
def postorder_trav(root):
    # res=[]
    if root is None:
        return
    print(root.data)
    postorder_trav(root.left)
    postorder_trav(root.right)


preorder_trav(root)
print()
postorder_trav(root)