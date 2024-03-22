class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for i in nums:
            if len(self.pq)<k:
                heapq.heappush(self.pq,i)
            elif self.pq[0]<i:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq,i)

                    

    def add(self, i: int) -> int:
        if self.k>len(self.pq):
            heapq.heappush(self.pq,i)
            return self.pq[0]

        if self.pq[0]<=i:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq,i)

        return self.pq[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)