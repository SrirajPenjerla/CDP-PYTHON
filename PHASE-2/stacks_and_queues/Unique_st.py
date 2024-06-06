# aabcdab
# a#bcd##

class Stack:
    def __init__(self):
        s=[]
        self.s=s
        
    def push(self,data):
        self.s.append(data)

    def pop(self):
        return self.s.pop()
    
    def top(self):
        return self.s[-1]
    
    def isempty(self):
        if len(self.s) == 0:
            return True
        else:
            return False
    def make_stack(self,arr):
        arr=arr[::-1]
        for i in arr:
            self.push(i)
def sol(str):
    st=Stack()
    for i in str:
        if i not in st.s:
            print(i,end=" ")
            st.push(i)
        else:
            print("#",end=" ")

sol("aabcdab")