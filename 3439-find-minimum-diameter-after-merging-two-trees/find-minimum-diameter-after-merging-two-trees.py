class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def adjlist(edges):
            d = {}
            for i,j in edges:
                if i not in d:
                    d[i] =[]
                if j not in d:
                    d[j]=[]
                d[i].append(j)
                d[j].append(i)
            return d
     
    

        def findmax(adj):
            k = 0
            def dfs(child,par):
                nonlocal k
                if child not in adj:return 0
                max_child = [0,0]
                for c in adj[child]:
                    if c == par:continue
                    heapq.heappush(max_child,dfs(c,child))
                    heapq.heappop(max_child)
                k = max(k,sum(max_child))
        
                return max(max_child)+1 
            dfs(0,-1)
            return k
        d1 = findmax(adjlist(edges1))
        d2 = findmax(adjlist(edges2))
        
        return max(d1,d2,1 + math.ceil(d1/2) + math.ceil(d2/2))


                

