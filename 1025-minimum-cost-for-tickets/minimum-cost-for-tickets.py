class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l = set(days)
        
        d = {}
        def dfs(i):
            if i>days[-1]:return 0
            if i in d:return d[i]
            if i not in l: return dfs(i+1)
            d[i] = min(costs[0] + dfs(i+1),costs[1] + dfs(i+7), costs[2] + dfs(i+30))
            return d[i]
        return dfs(0)
        
        
        
        d = [0]
        for i in range(1,days[-1]+1):
            if i not in l:
                d.append(d[-1])
            else:
                oneday = (d[i-1] if i-1>=0 else 0)+costs[0]
                sevenday = (d[i-7] if i-7>=0 else 0)+costs[1]
                thirtyday = (d[i-30] if i-30>=0 else 0) + costs[2]
                d.append(min(oneday,sevenday,thirtyday))
        return d[-1]

            



