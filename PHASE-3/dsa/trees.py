class Node:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None

class BST:
    def addNode(self,root,value):
        newNode=Node(value)
        if root == None:
            return newNode
        else:
            if value<root.data:
                if root.left!=None:
                    self.addNode(root.left,value)
                else:
                    root.left=newNode
            else:
                if root.right !=None:
                    self.addNode(root.right,value)
                else:
                    root.right=newNode
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data ,end= " ")
        if root.right!=None:
            self.inorder(root.right)
    def postorder(self,root):
        pass
    def preorder(self,root):
        pass
    def levelorder(self,root):
        q=[root]
        while q:
            ele=q.pop(0)
            print(ele.data,end=" ")
            if ele.left != None:
                q.append(ele.left)
            if ele.right != None:
                q.append(ele.right)


values=[10,55,54,23,4,0,2]
root=None
tree=BST()
root=tree.addNode(root,values[0])
for i in range(1,len(values)):
    tree.addNode(root,values[i])
tree.inorder(root)
print()
tree.levelorder(root)
