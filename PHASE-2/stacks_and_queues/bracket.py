s=input("Enter the string to validate :: ")
st=[]
for i in range(len(s)):
    if s[i] in "({[":
        st.append((s[i]))
    elif (st[-1]== "[" and s[i]=="]") or (st[-1]== "(" and s[i]==")") or (st[-1]== "{" and s[i]=="}") :
            st.pop()
    else:
        break
if st==[]:
    print("Valid")
else:
    print("Invalid")
