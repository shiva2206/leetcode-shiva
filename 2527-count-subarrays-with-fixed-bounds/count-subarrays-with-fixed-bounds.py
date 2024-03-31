class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        i = 0
        ans =0
        d ={}
        l = []
        pq = []
        c = 0
        for j in range(len(nums)):
            if nums[j]>maxK or nums[j]<minK:
                i = j+1
                d={}
                pq=[]
                c = 0
                l=[]
                continue
            if nums[j] not in d:
                d[nums[j]] = 0
                heapq.heappush(l,nums[j])
                heapq.heappush(pq,-nums[j])
            d[nums[j]]+=1
            while l and l[0] == minK and pq and -pq[0]==maxK:
                d[nums[i]]-=1
                if d[nums[i]] == 0:
                    d.pop(nums[i])
                while l and l[0] not in d:
                    heapq.heappop(l)
                while pq and -pq[0] not in d:
                    heapq.heappop(pq)
                c +=1  
                i+=1

            ans += c
        return ans