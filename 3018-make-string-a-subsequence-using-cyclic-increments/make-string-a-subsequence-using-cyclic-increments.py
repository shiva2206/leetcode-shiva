class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        d = set()
        def dfs(i,j):
            if j==len(str2):return True
            if i == len(str1) or len(str1)-i < len(str2)-j:return False
            if (i,j) in d: return False
            d.add((i,j))
            if str1[i]==str2[j] and dfs(i+1,j+1): return True
            elif ((ord(str1[i])+1)-97)%26 == ord(str2[j])-97 and dfs(i+1,j+1): return True
            return dfs(i+1,j)
        return dfs(0,0)
             