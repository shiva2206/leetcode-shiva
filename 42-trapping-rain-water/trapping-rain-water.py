class Solution:
    def trap(self, height: List[int]) -> int:

        leftmax = height[0]
        rightmax = height[-1]


        left = 0
        right = len(height)-1
        ans = 0
        while left <= right:
            if leftmax<rightmax:
                ans += max(0,leftmax -height[left])
                leftmax= max(leftmax,height[left])
                left+=1
            else:
                ans += max(0,rightmax - height[right])
                rightmax= max(rightmax,height[right])
                right-=1
            print(ans,left,right)
        return ans
