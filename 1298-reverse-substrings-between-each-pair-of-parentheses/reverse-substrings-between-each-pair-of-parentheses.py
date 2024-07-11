class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        s = "("+s+")"
        def dfs(i,j):

            q = ""

            while i<j:
                if s[i]=="(":
                    ans,end = dfs(i+1,j)
                    q = q+ans
                    i = end
                elif s[i]==")":
                    return [q[::-1],i]
                else:q+=s[i]

                i+=1    
            return q[::-1]
        return dfs(1,len(s)-1)[::-1]