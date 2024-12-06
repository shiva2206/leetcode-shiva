class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        
        i = 0
        odd = 0
        ans = 0
        c = 0
        for j in range(len(nums)):
            if nums[j]%2==1:
                odd+=1
                c = 0
            
            while i<len(nums) and odd == k :
                c+=1
                if nums[i]%2==1:
                    odd-=1
                i+=1
            ans+=c
        return ans
