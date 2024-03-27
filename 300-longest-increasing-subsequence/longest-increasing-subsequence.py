class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        l = [nums[0]]
        for i in nums[1:]:
            x = bisect.bisect_left(l,i)
            if x == len(l):
                l.append(i)
            else:
                l[x] = i
        return len(l)        

