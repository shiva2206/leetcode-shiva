class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for i in word:
            if i not in d:
                d[i]=0
            d[i]+=1
        l = list(d.keys())
        l.sort(key = lambda x : -d[x])

       
        ans = 0
        
        for i in range(len(l)):
            ans += ((i//8) +1)*d[l[i]]
        return ans

