class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = {}
        def dfs(i,j):
            if i == len(text1) or j == len(text2):return 0
            if (i,j) in d:return d[(i,j)]
            m = 0
            if text1[i]==text2[j]:
                m = 1 + dfs(i+1,j+1)
            else:
                m = max(m,dfs(i+1,j),dfs(i,j+1))
            d[(i,j)] =m
            return m
        return dfs(0,0)