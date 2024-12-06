class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = ["("]
        res = ""
        for i in s[1:]:
            if not l:
                l.append("(")
            elif i==")":
                l.pop()
                if l:
                    res+=")"
            else:
                if l:
                    res+="("
                l.append("(")
        return res

