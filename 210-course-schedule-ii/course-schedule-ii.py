class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        
        d = {}
        for i,j in pre:
            if i not in d:
                d[i] = []
            d[i].append(j)
        vis = {}
        res =[]
        def dfs(i):
            if i in vis:
                return vis[i]
            vis[i] = False
            
            if i in d:
                for j in d[i]:
                    if not dfs(j):return False
            res.append(i)
            vis[i] =True
            return True
        for i in range(num):
            if not dfs(i):return []
        return res        

