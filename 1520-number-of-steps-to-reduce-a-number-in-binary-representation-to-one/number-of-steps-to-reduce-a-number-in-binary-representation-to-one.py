class Solution:
    def numSteps(self, s: str) -> int:
        
        s = int(s,2)
        ans = 0
        while s>1:
            if s&1:
                s=s+1
            else:
                s//=2
            ans+=1
        return ans