class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        d = {0:-1}

        s = 0
        
        for i in range(len(nums)):
            s = (s+nums[i])%k
            if s in d:
                if i - d[s]>1:return True
            else:
                d[s] = i
        return False


        