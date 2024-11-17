class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        ans = 0
        j = 0
        i = 0
        p = j
        while True:
            for k in range(i,j+1):
                if k + nums[k]>=len(nums)-1:return ans+1
                p = max(p,k + nums[k])

            ans +=1
            i = j+1
            j = p
        return ans
                
