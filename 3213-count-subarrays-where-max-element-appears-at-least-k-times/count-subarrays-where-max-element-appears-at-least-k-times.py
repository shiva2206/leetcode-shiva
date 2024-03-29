class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        c = 1
        m = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>m:
                m = nums[i]
                c=1
            elif nums[i] == m:
                c+=1
        if c<k:return 0

        ans = 0
        i = 0
        k-=1
        t = 0
        for j in range(len(nums)):
            if nums[j]==m:
                t+=1
            while t>k:
                if nums[i]==m:
                    t-=1
                i+=1
            ans += (j-i+1)
        
        return len(nums)*(len(nums)+1)//2 - ans
