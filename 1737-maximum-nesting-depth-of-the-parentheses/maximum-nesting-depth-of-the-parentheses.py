class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        c = 0
        for i in s:
            if i=="(":
                c+=1
                ans=max(ans,c)
            elif i==")":
                c-=1
        return ans
            