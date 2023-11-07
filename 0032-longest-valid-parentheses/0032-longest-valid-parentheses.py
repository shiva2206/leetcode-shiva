class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=[]
        for i in range(len(s)):
            if s[i]=="(":
                l.append(i)
            else:
                if l and  s[l[-1]]=="(":
                    l.pop()
                else:
                    l.append(i)
        if not l:return len(s)
        m=l[0]
        for i in range(len(l)-1):
            m=max(m,l[i+1]-l[i]-1)
        m=max(m,len(s)-l[-1]-1)      
        print(l)      
        return m  
        