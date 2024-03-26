class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        d=defaultdict(lambda : -1)
        def dfs(i,j):
            if i == len(str1) or j==len(str2):return 0
            if (i,j) in d:return d[(i,j)]

            if str1[i] == str2[j]:
                m = 1 + dfs(i+1,j+1)
            else:
                m = max(dfs(i+1,j),dfs(i,j+1))

            d[(i,j)] = m 
            return m
        p = dfs(0,0)
        res =""
        i = 0
        j = 0

        while i<len(str1) and j<len(str2):
            if str1[i] == str2[j]:
                res += str1[i]
                i+=1
                j+=1
            elif d[(i,j+1)]<d[(i+1,j)]:
                res += str1[i]
                i+=1
            else:
                res +=str2[j]
                j+=1
        if i<len(str1):
            res+=str1[i:]
        else:
            res+=str2[j:]            
        return res            
