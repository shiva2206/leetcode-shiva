class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for i in nums:
            if len(pq)<k:
                heapq.heappush(pq,i)
            elif pq[0]<i:
                heapq.heappop(pq)
                heapq.heappush(pq,i)
        return pq[0]        