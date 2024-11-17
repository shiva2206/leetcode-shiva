class Solution:
    def canJump(self, nums: List[int]) -> bool:
         
        j = 0
        i=0
        while i<=j:
            j = max(j,i + nums[i])
            if j>=len(nums)-1:return True
            i+=1
        return False