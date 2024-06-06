class Stack:
    def __init__(self):
        s=[]
        self.s=s
    def push(self,data):
        self.s.append(data)
    def pop(self):
        # a=self.s.pop()
        # print(self.s)
        return self.s.pop()
    def top(self):
        return self.s[-1]
    def isempty(self,a):
        if len(a) == 0:
            # print(1)
            return True
        else:
            # print(0)
            return False
    def display(self):
        b=self.s
        while self.isempty(b)!=True:
            print(self.pop())
    def peek(self,pos):
        print(self.s[pos])
    
    def rev(self):
        b=Stack()
        while len(self.s)!=0:
            a=self.pop()
            b.push(a)
        b.display()
    def rev_no_space(self):
        i=0
        while i<len(self.s):
            self.peek(i)
            i+=1


st=Stack()  
st.push("hello")
st.push(112)
st.push(45)
# st.display()
st.rev_no_space()