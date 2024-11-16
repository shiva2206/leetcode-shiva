class Solution:
    def combinationSum(self, cand: List[int], tar: int) -> List[List[int]]:
        res = []
        s = []
        def dfs(i,t):
            if i>=len(cand) or t>tar:return
            if  t==tar:
                res.append(s.copy())
                return 
            dfs(i+1,t)
            s.append(cand[i])
            dfs(i,t+cand[i])
            s.pop()
        dfs(0,0)
        return res

        