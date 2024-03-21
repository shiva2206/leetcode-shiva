class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        q = sum(piles)
        d={}
        def dfs(i,j,k):
            if i>j:return 0
            if(i,j) in d:return d[(i,j)]

            if k==0:
                d[(i,j)] = max(piles[i] + dfs(i+1,j,1), piles[j] + dfs(i,j-1,1))
            else:
                d[(i,j)]  = min(dfs(i+1,j,0),dfs(i,j-1,0))
            return d[(i,j)]
        return dfs(0,len(piles)-1,0)           