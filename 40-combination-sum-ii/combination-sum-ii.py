class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        cand.sort()
        res = []
        s =[]
        def dfs(i,j):
            if j>target:return 
            if i == len(cand):
                if j==target:
                    res.append(s.copy())
                return 
           
            x = i+1
            while x<len(cand):
                if cand[x]!=cand[i]:break
                x+=1
            dfs(x,j)

            s.append(cand[i])
            dfs(i+1,j+cand[i])
            s.pop()
            return 
        dfs(0,0)
        return res    
               