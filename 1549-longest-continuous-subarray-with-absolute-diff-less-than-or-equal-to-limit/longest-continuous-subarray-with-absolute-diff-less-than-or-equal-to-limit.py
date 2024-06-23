class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxpq =[]
        minpq =[]

        ans = 0
        i = 0
        for j in range(len(nums)):
            heapq.heappush(maxpq,(-nums[j],j))
            heapq.heappush(minpq,(nums[j],j))
            while maxpq and minpq and -maxpq[0][0] - minpq[0][0]>limit:
                i+=1
                while maxpq and maxpq[0][1]<i:
                    heapq.heappop(maxpq)
                while minpq and minpq[0][1]<i:
                    heapq.heappop(minpq)
            ans = max(ans,j-i+1)
        return ans
            
