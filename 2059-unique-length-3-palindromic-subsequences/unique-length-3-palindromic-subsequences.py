class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
    
        first = {}
        last = {}
        for j,i in enumerate(s):
            if i not in first:
                first[i] = j
            else:
                last[i] = j
        ans = 0
      
        for i in range(97,123):
            c = chr(i)
            if c not in last:continue
            q = s[ first[c]+1 : last[c] ] 
            ans += len(set(q))

        return ans