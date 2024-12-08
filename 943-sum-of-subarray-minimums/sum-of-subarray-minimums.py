class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        
        nse = [len(nums)-i for i in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                x = stack.pop()
                nse[x] = i-x
            stack.append(i)
        
        pse = [len(nums) - i for i in range(len(nums)-1,-1,-1)]
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                x = stack.pop()
                pse[x] = x - i
            stack.append(i)
        print(nse)
        print(pse)
        ans =0

        for i in range(len(nums)):
            ans += (nums[i]*nse[i]*pse[i])%1000000007
        return ans%1000000007