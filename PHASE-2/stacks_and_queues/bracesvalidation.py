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
        
s=input("Enter the string to validate :: ")
st=Stack()
for i in range(len(s)):
    if s[i] in "({[":
        st.push(s[i])
    elif (st.top()== "[" and s[i]=="]") or (st.top()== "(" and s[i]==")") or (st.top()== "{" and s[i]=="}") :
            st.pop()
    else:
        break
if st.isempty():
    print("Valid")
else:
    print("Invalid")
