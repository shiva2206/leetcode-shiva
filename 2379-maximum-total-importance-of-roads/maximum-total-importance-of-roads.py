class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        for i,j in roads:
            if i not in d:
                d[i]=0
            if j not in d:
                d[j]=0
            d[i]+=1
            d[j]+=1
        l = sorted(d.values(),reverse = True)
        ans = 0
        for i in l:
            ans += n*i
            n-=1
        return ans
