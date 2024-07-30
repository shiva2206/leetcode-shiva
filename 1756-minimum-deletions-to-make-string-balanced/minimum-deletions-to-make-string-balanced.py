class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = -1
        b = -1
        
        for i in range(len(s)):
            if s[i]=='a':
                a = i
            else:
                if b == -1:
                    b = i
        
        xa = 0
        xb = 0
        for i in range(b,a+1):
            if s[i]=='a':
                xa+=1
            else:
                xb+=1
        ya = yb = 0
        ans = min(xa,xb)
        for i in range(b,a+1):
            if s[i]=='b':
                
                ans = min(ans,yb + xa - ya )
                yb+=1
            else:
                ya+=1
        return ans
            
