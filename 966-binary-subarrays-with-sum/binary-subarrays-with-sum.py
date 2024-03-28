class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0:1}
        ans = 0
        s = 0
        for i in nums:
            s+=i
            if s - goal in d:
                ans += d[s-goal]
            if s not in d:
                d[s]=0
            d[s] +=1
        return ans