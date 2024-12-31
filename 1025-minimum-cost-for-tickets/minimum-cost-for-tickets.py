class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

     

        d = [[0]*(len(days)+1) for i in range(days[-1]+31)]

        for i in range(days[-1]-1,-1,-1):
            for j in range(len(days)-1,-1,-1):
                if i>=days[j]:
                    d[i][j] = d[i][j+1]
                else:
                    d[i][j] = float('inf')
                    m = min(costs[0] + d[i+1][j],costs[1] + d[i+7][j] ,costs[2] + d[i+30][j],d[days[j]-1][j])
                    d[i][j] = m
        return d[0][0]
            



