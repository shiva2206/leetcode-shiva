class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        ans = 0
        minque = deque()
        maxque = deque()

        i=0
        for j in range(len(nums)):
            while minque and nums[minque[-1]]>nums[j]:
                minque.pop()
            
            while maxque and nums[maxque[-1]]<nums[j]:
                maxque.pop()
            
            minque.append(j)
            maxque.append(j)

            while nums[maxque[0]] - nums[minque[0]] > 2:
                i+=1
                if maxque and i>maxque[0]: 
                    maxque.popleft()
                if minque and i>minque[0]:
                    minque.popleft()
            ans += j-i+1
        return ans