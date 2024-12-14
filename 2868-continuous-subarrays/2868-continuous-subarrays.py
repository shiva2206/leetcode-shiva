class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        i = 0
        
        maxque = deque()
        minque =deque()
        ans = 0
        j = 0
        for j in range(len(nums)):
            # while maxque and i>maxque[0]:
            #     maxque.popleft()
            # while minque and i>minque[0]:
            #     minque.popleft()
            
            while maxque and nums[maxque[-1]] < nums[j]:
                maxque.pop()
            while minque and nums[minque[-1]] > nums[j]:
                minque.pop()
            minque.append(j)
            maxque.append(j)
            
            while (nums[maxque[0]]- nums[minque[0]])>2:
                # print(i)
                i+=1
                if maxque and i>maxque[0]:
                    maxque.popleft()
                if minque and i>minque[0]:
                    minque.popleft()
            ans += j-i+1
            # print(i,j,minque,maxque,j-i+1)
        return ans