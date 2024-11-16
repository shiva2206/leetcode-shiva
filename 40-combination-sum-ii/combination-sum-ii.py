class Solution:
    def combinationSum2(self, cand: List[int], tar: int) -> List[List[int]]:
        
        cand.sort()
        res = []
        s = []
        def dfs(i,t):
            if t==tar:
                res.append(s.copy())
                print(s)
                return 
            if i==len(cand) or t>tar:
                print(s)
                return
            s.append(cand[i])
            dfs(i+1,t+cand[i])
            s.pop()
            x=i
            while x+1<len(cand) and cand[x+1]==cand[i]:
                x+=1
            dfs(x+1,t)
        dfs(0,0)
        return res