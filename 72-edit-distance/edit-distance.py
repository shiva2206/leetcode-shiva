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

        d = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(word1),-1,-1):
            for j in range(len(word2),-1,-1):
                if j == len(word2):
                    d[i][j] = len(word1)-i
                    continue
                if i ==len(word1):
                    d[i][j] = len(word2) - j
                    continue
                m = 0
                if word1[i] == word2[j]:
                    m = d[i+1][j+1]
                else:
                    m =1 + min(d[i+1][j],d[i][j+1],d[i+1][j+1])
                d[i][j] = m


        return d[0][0]
