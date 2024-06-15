class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprof=[]
        mincap=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(mincap)

        for i in range(k):
            while mincap and mincap[0][0]<=w:
                c,p = heapq.heappop(mincap)
                heapq.heappush(maxprof,-1*p)

            if not maxprof:
                break

            w+=-1*heapq.heappop(maxprof)
        return w       