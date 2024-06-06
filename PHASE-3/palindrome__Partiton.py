'''
LINK:: https://leetcode.com/problems/palindrome-partitioning/description/


Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

def Back_track(ans,st,n,f):
    if n == len(st):
        f.append(ans[:])
        return 
    print(ans)
    curr=""
    for pos in range(n,len(st)):
        curr+=st[pos]
        if curr == curr[::-1]:
            ans.append(curr)
            Back_track(ans,st,pos+1,f)
            ans.pop()

    


f=[]
Back_track([],"aab",0,f)
print(f)