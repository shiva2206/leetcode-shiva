class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    
        res = ""
        c = 0
        for i in s:
            if i=="(":
                if c==0:
                    pass
                else:
                    res+="("
                c+=1

            else:
                c-=1
                if c!=0:
                    res +=")"
                
        return res

