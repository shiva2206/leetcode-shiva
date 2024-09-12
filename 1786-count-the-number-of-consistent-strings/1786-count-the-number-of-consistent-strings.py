class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        d = {}
        for i in allowed:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        ans = 0
        for i in words:
            
            for j in i:
                if j not in d:
                    ans -=1
                    break
            ans+=1
        return ans