class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        d = set()
        
        l=[(arr[0]/arr[len(arr)-1],0,len(arr)-1)]

        while k>1:
            # print(l)

            a,x,y = heapq.heappop(l)
    
            if (x+1,y) not in d:        
                heapq.heappush(l,(arr[x+1]/arr[y],x+1,y))
                d.add((x+1,y))
            if(x,y-1) not in d:
                heapq.heappush(l,(arr[x]/arr[y-1],x,y-1))
                d.add((x,y-1))
            k-=1
        # print(l)    
        ans = heapq.heappop(l)
        return [arr[ans[1]],arr[ans[2]]]

