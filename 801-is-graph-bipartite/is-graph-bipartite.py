class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d={}
        def dfs(t,k):
            if t in d:return d[t]==k
            d[t] = k

            for i in graph[t]:
                if not dfs(i,not k):return False
            return True
        for i in range(len(graph)):
            if i not in d and not dfs(i,True):return False    
        return True