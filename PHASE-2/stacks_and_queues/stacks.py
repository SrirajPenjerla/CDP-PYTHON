class Stack:
    def __init__(self):
        s=[]
        self.s=s
    def push(self,data):
        self.s.append(data)
    def pop(self):
        a=self.s.pop()
        return a
    def top(self):
        return self.s[-1]
    def isempty(self):
        if len(self.s) == 0:
            return False
        else:
            return True
    def display(self):
        while self.isempty():
            print(self.pop())
    
st=Stack()
st.push(12)
st.push(112)
st.push(45)
st.display()
st.pop()
st.display()
print(st.top())