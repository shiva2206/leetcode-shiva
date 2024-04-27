class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
         
        l = defaultdict(list)
        for i in range(len(ring)):
            l[ring[i]].append(i)
        d={}
        def dfs(i,j):
            if i==len(key):return 0
            if (i,j) in d:return d[(i,j)]
            d[(i,j)] = float('inf')

            for k in l[key[i]]:
                if k == j:
                    d[(i,j)] = min(d[(i,j)], dfs(i+1,k))
                elif k<j:
                    x = j-k
                    y = k + len(ring) - j
                    d[(i,j)] = min(d[(i,j)], min(x,y) + dfs(i+1,k))
                else:
                    x = k-j
                    y = j + len(ring) - k
                    d[(i,j)] = min(d[(i,j)],min(x,y) + dfs(i+1,k))
            return d[(i,j)]        

        return dfs(0,0) + len(key)        
