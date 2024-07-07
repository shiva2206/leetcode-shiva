class Solution:
    def numWaterBottles(self, tles: int, num: int) -> int:
        ans = tles
        while tles>=num:
            ans += tles//num
            tles = tles//num + tles%num
        return ans
