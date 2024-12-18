class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        sta = []
        
        for i in range(len(prices)):
            while sta and prices[sta[-1]]>=prices[i]:
                
                prices[sta.pop()] -= prices[i]
            
            sta.append(i)
        return prices
        