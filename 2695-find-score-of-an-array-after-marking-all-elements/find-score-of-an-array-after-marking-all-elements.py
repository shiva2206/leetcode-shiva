class Solution:
    def findScore(self, nums: List[int]) -> int:
        d = set()
        ans = 0
        hp = []
        for i,j in enumerate(nums):
            hp.append((j,i))
        heapq.heapify(hp)

        while hp:
            val,i = heapq.heappop(hp)
            if i in d:continue
            ans+=val
            if i-1>=0 and i-1 not in d:
                d.add(i-1)
            if i+1<len(nums) and i+1 not in d:
                d.add(i+1)
        return ans