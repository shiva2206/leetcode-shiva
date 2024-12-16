class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = []
        for i in range(len(nums)):
            hp.append((nums[i],i))
        heapq.heapify(hp)

        for i in range(k):
            val,i = heapq.heappop(hp)
            nums[i] = val*multiplier
            heapq.heappush(hp,(val*multiplier,i))
        return nums