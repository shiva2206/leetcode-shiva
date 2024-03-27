class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        s = 0
        for i in range(k):
            s+=card[i]
        k-=1
        ans = s
        while k>=0:
            s -= card[k]
            s+=card.pop()
            ans = max(ans,s)
            k-=1    
        return ans    