class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        m = max(nums)
        ans = 0
        i = 0
        l=0
        t = 0
        for j in nums:
            if j == m:
                t+=1
            while t == k:
                if nums[i]==m:
                    t-=1
                i+=1
                l+=1
            ans +=l
        return ans
