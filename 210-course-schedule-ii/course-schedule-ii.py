class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        d =defaultdict(list)
        for i,j in pre:
            d[j].append(i)
        
        vis = {}
        res =[]
        def dfs(i):
            if i in vis:
                return vis[i]
            vis[i] = True
            for j in d[i]:
                if dfs(j):return True
            res.append(i)
            vis[i] = False
            return False
        for i in range(num):
            if dfs(i):return []
        return res[::-1]
