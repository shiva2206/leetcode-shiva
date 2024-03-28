class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        ans = 0
        s =0 
        c = 0
        for j in range(len(nums)):
            if nums[j]%2==1:
                s +=1
                c =0
        
            if s == k:
                
                while i<len(nums) and nums[i]%2==0:
                    c+=1
                    i+=1
                s-=1
                c+=1
                i+=1
            ans += c
        return ans