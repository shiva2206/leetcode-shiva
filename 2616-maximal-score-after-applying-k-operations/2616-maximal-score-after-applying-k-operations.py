class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = []
        for i in nums:
            if len(hp)<k:
                heapq.heappush(hp,i)
            elif hp[0]<i:
                heapq.heappush(hp,i)
                heapq.heappop(hp)
        l = []
        for i in hp:
            heapq.heappush(l,-i)
        ans = 0
        for i in range(k):
            x = heapq.heappop(l)
            x = -x
            ans += x
            heapq.heappush(l,-math.ceil(x/3))
        return ans
            

            