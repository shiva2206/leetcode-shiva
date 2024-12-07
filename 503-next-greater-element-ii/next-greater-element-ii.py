class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res =[-1]*len(nums)
        stack = []
        for i in range(len(nums)*2-1):
            x = i%len(nums)
            while stack and nums[stack[-1]]<nums[x]:
                y = stack.pop()
                res[y] = nums[x]
            stack.append(x)
        return res