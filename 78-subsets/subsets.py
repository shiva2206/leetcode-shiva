class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(2**(len(nums))):
            x = i
            s =[]
            for j in range(len(nums)):
                if x&1==1:
                    s.append(nums[j])
                x>>=1
            res.append(s.copy())
        return res