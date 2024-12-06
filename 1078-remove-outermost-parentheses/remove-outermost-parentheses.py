class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    
        res = ""
        c = 0
        for i in s:
            if i=="(":
                c+=1
                if c!=1:
                    
                    res+="("
                

            else:
                c-=1
                if c!=0:
                    res +=")"
                
        return res

