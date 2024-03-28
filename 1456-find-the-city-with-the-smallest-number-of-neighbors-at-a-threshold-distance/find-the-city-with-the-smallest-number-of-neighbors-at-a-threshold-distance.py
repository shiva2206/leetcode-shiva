class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], thre: int) -> int:
         
        d = {}
        for i,j,k in edges:
            if i not in d:
                d[i] =[]
            if j not in d:
                d[j] = []
            d[i].append((k,j))
            d[j].append((k,i))

        main = [0]*n
        for i in range(n):
            dis = [float('inf')]*n    
            l =[(0,i)]
            dis[i]=0
            while l:
                x,y = heapq.heappop(l)
                if y not in d:continue
                for a,b in d[y]:
                    m = x+a
                    if dis[b]>m and m<=thre:
                        dis[b] = m
                        heapq.heappush(l,(m,b))
            
            for w in range(n):
                if dis[w]<=thre:
                    main[w]+=1
        ans = n-1
        m = main[n-1]
        print(main)
        for i in range(n):
            if m>=main[i]:
                m = main[i]
                ans = i
        return ans
