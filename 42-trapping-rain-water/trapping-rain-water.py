class Solution:
    def trap(self, hei: List[int]) -> int:
        
        l = 0
        r = len(hei)-1
        leftmax = hei[0]
        rightmax = hei[-1]
        ans = 0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(leftmax,hei[l])
                ans += leftmax - hei[l] 
            else:
                r-=1
                rightmax = max(rightmax,hei[r])
                ans += rightmax-hei[r]
        return ans