class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        for i in nums:
            k = k^i
        
        c= 0
        while k>0:
            c+=1
            k = k&(k-1)
        return c
       