class Solution:
    def numSteps(self, s: str) -> int:

        ans = 0
        c = 0
        for i in range(len(s)-1,0,-1):
            if s[i]=='0':
                if c == 0:
                    ans+=1
                else:
                    ans+=2
            else:
                if c == 0:
                    c=1
                    ans+=2
                else:
                    ans+=1
        return ans if c==0 else ans+1
            