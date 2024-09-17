class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for i in s1.split():
            if i not in d:
                d[i]=0
            d[i]+=1
        
        for j in s2.split():
            if j not in d:
                d[j] = 0
            d[j]+=1
        l = []
    
        for i in d.keys():
            if d[i]==1:
                l.append(i)
        return l
        