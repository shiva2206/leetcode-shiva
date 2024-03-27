class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        

        words.sort(key = lambda x: len(x))
        dp = defaultdict(int)
        m = 0
        for i in words:
            for j in range(len(i)):
                s = i[:j] + i[j+1:]
                dp[i] = max(dp[i],1 + dp[s])
                m = max(m,dp[i])
        return m