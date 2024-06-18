class Solution:
    def maxProfitAssignment(self, diff: List[int], prof: List[int], work: List[int]) -> int:
        
        l=[]
        for i in range(len(diff)):
            l.append((diff[i],-prof[i]))
        l.sort()

        pq = []
        work.sort()
        j = 0
        ans = 0
        for i in work:
            while j<len(l) and l[j][0]<=i:
                heapq.heappush(pq,l[j][1])
                j+=1
            
            if pq :
                
                ans -= pq[0]
        return ans



