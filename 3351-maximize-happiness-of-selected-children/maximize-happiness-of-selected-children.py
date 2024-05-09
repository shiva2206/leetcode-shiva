class Solution:
    def maximumHappinessSum(self, happ: List[int], k: int) -> int:
        
        happ.sort(reverse = True)
        ans = 0
        for i in range(k):
            ans += max(happ[i]-i,0)
        return ans