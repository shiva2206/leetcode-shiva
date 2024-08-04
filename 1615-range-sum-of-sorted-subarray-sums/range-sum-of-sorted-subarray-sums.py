class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        hp = [(nums[i],i) for i in range(len(nums))]
        hp.sort()
        res = 0
        for i in range(right):
            x,y = heapq.heappop(hp)
            if i>=left -1:
                res = (res + x) % (1000000007)
            if y+1<len(nums):
                heapq.heappush(hp,(x + nums[y+1],y+1))
        return res