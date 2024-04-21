class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        
        vis = set()
        def dfs(i):
            if i == destination:return True
            if i in vis:return False
            vis.add(i)
            for j in d[i]:
                if dfs(j): return True
            return False
        return dfs(source)

