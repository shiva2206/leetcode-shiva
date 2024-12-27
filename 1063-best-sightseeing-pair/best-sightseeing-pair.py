class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
       m = values[-1] - (len(values)-1)
       ans = 0
       for i in range(len(values)-2,-1,-1):
           ans =max(ans,values[i] + i  + m)
           m = max(m,values[i]-i)
       return ans
              