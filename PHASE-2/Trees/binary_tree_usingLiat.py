class BinaryTree:
    def __init__(self,size):
        self.lis=[0]*size
        self.lastindex=0
        self.size=size
    def insert(self,data):
        if self.lastindex == self.size:
            print("Tree is full ")
        self.lis[self.lastindex]=data
        self.lastindex=self.lastindex+1
        print("Inserted successfully")

a=BinaryTree(10)
a.insert(10)
a.insert(50)
a.insert(90)
a.insert(120)

print(a.lis[:])
