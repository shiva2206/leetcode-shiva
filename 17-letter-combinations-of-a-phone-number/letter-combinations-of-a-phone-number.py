class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        d = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = []

        def dfs(i,s):
            if i == len(digits):
                ans.append(s)
                return 
            for j in d[int(digits[i])-2]:
                dfs(i+1,s+j)
        dfs(0,"")
        return ans