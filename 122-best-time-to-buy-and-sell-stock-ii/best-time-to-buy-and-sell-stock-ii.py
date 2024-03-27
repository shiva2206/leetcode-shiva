class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i = prices[0]
        for j in prices[1:]:
            if i<j:
                
            
                m+= j-i
            i = j
        return m