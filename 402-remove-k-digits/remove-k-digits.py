class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for i in range(len(num)):
            while k>0 and stack and num[stack[-1]] >num[i]:
                k-=1
                stack.pop()
            stack.append(i)
        while k>0:
            stack.pop()
            k-=1
        res = ""
        for i in stack:
            if not res and num[i]=='0':continue
            res += num[i]
        return res if res else "0"
        
        