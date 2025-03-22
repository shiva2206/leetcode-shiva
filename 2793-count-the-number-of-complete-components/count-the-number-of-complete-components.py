class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        ran = [1] * n
        tot =[0] * n 
        def find(x):
            if par[x]!=x:
                 par[x] = find(par[x])
            return par[x]
        
        def union(x,y):

            tot[x]+=1
            tot[y]+=1

            p1 = find(x)
            p2 = find(y)

            if p1==p2:
                return 
            if ran[p1]<ran[p2]:
                ran[p2]+=ran[p1]
                par[p1] = p2
            else:
                ran[p1]+= ran[p2]
                par[p2] = p1
        for i,j in edges:
            union(i,j)
        
        d = {}
        for i in range(n):
            x = find(i)
            if x not in d:
                d[x] = []
            d[x].append(i)
        
        ans = 0
        for i in d:
            for j in d[i]:
                if tot[j] != len(d[i])-1:
                    break
            else:
                ans+= 1
        print(d)
        print(tot)
        return ans