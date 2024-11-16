class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0]
        p = 1

        for i in range(1,n+1):
            if p * 2 == i:
                p = i
            dp.append(1 + dp[i - p])
        return dp