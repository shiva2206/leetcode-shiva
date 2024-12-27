class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        plus = []
        minus = []
        for i in range(len(values)):
            plus.append(values[i]+i)    
            minus.append(values[i]-i)
        
        m = minus[-1]
        for i in range(len(minus)-2,-1,-1):
            m = max(minus[i],m)
            minus[i] = m
        ans = 0
        for i in range(len(plus)-1):
            ans = max(ans,plus[i]+minus[i+1])
        return ans