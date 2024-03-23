class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res =[]
        heig = []
        for i,j in enumerate(tasks):
            heig.append((j[0],j[1],i))
        t=0
        heapq.heapify(heig)
        pq = []

        while heig or pq:
            while heig and t>=heig[0][0]:
                x,y,z = heapq.heappop(heig)
                heapq.heappush(pq,(y,z))
            if pq:
                y,z = heapq.heappop(pq)

                t += y
                res.append(z)
            else:
                if heig:
                    t = heig[0][0]
        return res                
