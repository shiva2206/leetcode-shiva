class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = set()
        def dfs(i):
            if i in d:
                return 
            d.add(i)

            for x,y in enumerate(isConnected[i]):
                if y==1 and x!=i:
                    dfs(x) 
            return 
        ans = 0
        for i in range(len(isConnected)):
            if i not in d:
                dfs(i)
                ans+=1
        return ans