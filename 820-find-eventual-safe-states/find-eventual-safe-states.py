class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res =[]
        

        d={}
        def dfs(i):
            if i in d:return d[i]
            d[i] = False

            for j in graph[i]:
                if not dfs(j):return False
            d[i] =True
            return True
        for i in range(len(graph)):
            if dfs(i):res.append(i)
        return res
