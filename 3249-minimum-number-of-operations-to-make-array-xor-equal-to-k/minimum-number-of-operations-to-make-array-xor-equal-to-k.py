class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        a = 0
        for i in nums:
            a = a^i
        ans = 0
        while a>0 and k>0:
            if a&1 != k&1:
                ans+=1
            a = a>>1
            k = k>>1
        print(ans)
        while a>0:
            ans+= a&1
            a = a>>1
        while k>0:
            ans+=k&1
            k = k>>1
        return ans