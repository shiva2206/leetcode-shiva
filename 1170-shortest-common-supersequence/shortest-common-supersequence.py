class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # d = {}
        # def dfs(i,j):
        #     if i == len(str1): return len(str2) - j
        #     if j == len(str2):return len(str1) - i
        #     if (i,j) in d: return d[(i,j)]
        #     m = 0
        #     if str1[i] == str2[j]:
        #         m = 1 + dfs(i+1,j+1)
        #     else:
        #         m = 1 + min(dfs(i,j+1),dfs(i+1,j))
        #     d[(i,j)] =m
        #     return m
        #  ans =  dfs(0,0)
        d = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
        for i in range(len(str1)):
            d[i][len(str2)] = len(str1)-i

        for j in range(len(str2)):
            d[len(str1)][j] = len(str2)-j 

        for i in range(len(str1)-1,-1,-1):
            for j in range(len(str2)-1,-1,-1):
                if str1[i] == str2[j]:
                        m = 1 + d[i+1][j+1]
                else:
                        m = 1 + min(d[i][j+1],d[i+1][j])
                d[i][j] =m
                
        print(d)
        res = ""

        i = 0
        j = 0
        while i<len(str1) and j<len(str2):
            if str1[i] == str2[j]:
                res += str1[i]
                i+=1
                j+=1
            elif d[i][j+1] < d[i+1][j]:
                res += str2[j]
                j+=1
            else:
                res += str1[i]
                i+=1
            print(res,i,j)
        
        print(str1[i:],str2[j:])
        return res + str1[i:] + str2[j:]