class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        hp = []
        res = [-1]*len(queries)
        d = {}
        for i in range(len(queries)):
            x,y = queries[i]
            if x>y:
                x,y = y,x
            h1 = heights[x]
            h2 = heights[y]
            if h1 < h2 or x==y:
                res[i] = y
            else:
                if y not in d:
                    d[y] = []
                d[y].append((h1,i))
        for i,h in enumerate(heights):

            while i in d and d[i]:
                heapq.heappush(hp,d[i].pop())
            while hp and hp[0][0]<h:
                _,x = heapq.heappop(hp)
                res[x] = i
        return res
            

