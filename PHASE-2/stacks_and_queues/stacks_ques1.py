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

    def print_res(self):
        l=[]
        while self.isempty() != True:
            b=self.pop()
            if self.isempty() ==True:
                l.append(-1)
                break
            else:
                c=self.top()
                if b < c:
                    l.append(c)
                else:
                    l.append(-1)
        print(l)

def next_greater_ele(arr):
        n=len(arr)
        ans=[-1]*n
        st=Stack()
        st.push(-1)
        # print(st.top())
        for i in range(n-1,-1,-1):
            curr=arr[i]
            while st.top()!=-1 and st.top()<=curr:
                st.pop()
            ans[i]=st.top()
            st.push(curr)
        return ans

def next_smaller_ele(arr):
        n=len(arr)
        ans=[-1]*n
        st=Stack()
        st.push(-1)
        # print(st.top())
        for i in range(n-1,-1,-1):
            curr=arr[i]
            while st.top()!=-1 and st.top()>=curr:
                st.pop()
            ans[i]=st.top()
            st.push(curr)
        return ans
def prev_greater_ele(arr):
        n=len(arr)
        ans=[-1]*n
        st=Stack()
        st.push(-1)
        # print(st.top())
        for i in range(n):
            curr=arr[i]
            while st.top()!=-1 and st.top()<=curr:
                st.pop()
            ans[i]=st.top()
            st.push(curr)
        return ans

def prev_smaller_ele(arr):
        n=len(arr)
        ans=[-1]*n
        st=Stack()
        st.push(-1)
        # print(st.top())
        for i in range(n):
            curr=arr[i]
            while st.top()!=-1 and st.top()>=curr:
                st.pop()
            ans[i]=st.top()
            st.push(curr)
        return ans

print(next_greater_ele([2,14,16,1,4,12]))
print(next_smaller_ele([2,14,16,1,4,12]))
print(prev_greater_ele([2,14,16,1,4,12]))
print(prev_smaller_ele([2,14,16,1,4,12]))
# st=Stack()
# st.make_stack()
# st.print_res()