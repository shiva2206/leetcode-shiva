class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        
        d = defaultdict(list)
        for i,j in pre:
            d[j].append(i)
        
        vis = {}
        def dfs(i):
            if i in vis:
                return vis[i]
            vis[i] = True
            for j in d[i]:
                if dfs(j):return True

            vis[i] = False
            return False
        
        for i in range(num):
            if dfs(i):return False
        return True
