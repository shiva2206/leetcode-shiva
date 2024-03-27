class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
    #    if k>len(card):return 0
       n = len(card) - k 
       t = sum(card)

       s = 0
       for i in range(n):
            s += card[i]
       ans = s
       i = 0
       for j in range(n,len(card)):
            s +=card[j]
            s -=card[i]
            i+=1
            ans = min(s,ans)
       return t - ans     