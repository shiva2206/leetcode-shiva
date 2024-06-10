class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l = heights +[]
        l.sort()

        ans = 0
        for i in range(len(l)):
            ans += (1 if l[i]!=heights[i] else 0)
        return ans