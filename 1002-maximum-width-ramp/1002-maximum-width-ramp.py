class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        sta = []
        for i,x in enumerate(nums):

                if not sta or nums[sta[-1]]>x:
                    sta.append(i)
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            x = nums[i]
            while sta and nums[sta[-1]]<=x:
                ans = max(ans,i - sta.pop())
        return ans