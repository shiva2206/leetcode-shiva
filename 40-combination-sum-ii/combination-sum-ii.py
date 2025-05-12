class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        
        cand.sort()
        ans = []
        s = []
        def dfs(i,t):
            if t == target:
                ans.append(s.copy())
                return

            if t> target or i == len(cand):
                return 
            s.append(cand[i])
            dfs(i+1,t + cand[i])
            s.pop()
            x = cand[i]
            while i<len(cand) and cand[i] == x:
                i+=1
            dfs(i,t)
        dfs(0,0)
        return ans