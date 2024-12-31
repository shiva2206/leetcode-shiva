class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        d = {}
        def dfs(i,j):
            if j == len(days):return 0
            if i>=days[j]:return dfs(i,j+1)
            if (i,j) in d:return d[(i,j)]
            d[(i,j)] = float('inf')
            m = min(costs[0] + dfs(i+1,j),costs[1] + dfs(i+7,j) ,costs[2] + dfs(i+30,j),dfs(days[j]-1,j))
            d[(i,j)] = m 
            return m
        return dfs(0,0)
            



