class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        
      
        d = [0]*(high+1+max(one,zero))
        for c in range(high,-1,-1):
            m = 1 if low<=c <=high else 0
            m += (d[c+one] +d[c+zero])%1000000007
            d[c] = m

        return d[0]