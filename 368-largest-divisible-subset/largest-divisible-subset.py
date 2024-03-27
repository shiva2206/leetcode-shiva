class Solution:
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        self.start = -1
        self.ans = 0    
        d = {}
        has = {}
        nums.sort()
        def dfs(i):
            if i in d: return d[i]
            d[i] = 1

            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    m = 1 + dfs(j)
                    if m>d[i]:
                        d[i] = m
                        has[i] = j
            if self.ans<d[i]:
                self.ans = d[i]
                self.start = i
            return d[i]
        for i in range(len(nums)):
            dfs(i)
  
        
        res = [nums[self.start]]
        while self.start in has:
            self.start = has[self.start]
            res.append(nums[self.start])
        return res

        res.append()