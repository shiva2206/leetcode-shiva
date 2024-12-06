class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        d = {}
        def dfs(i,j):
            if j == len(word2):return len(word1) - i
            if i ==len(word1):return len(word2) - j
            if (i,j) in d:return d[(i,j)]
            m = 0
            if word1[i] == word2[j]:
                m = dfs(i+1,j+1)
            else:
                m =1 + min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))
            d[(i,j)] = m 
            return m
        return dfs(0,0)
