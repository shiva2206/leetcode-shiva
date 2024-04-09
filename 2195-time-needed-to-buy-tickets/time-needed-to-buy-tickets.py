class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
         
        ans = 0
        t = tickets[k]

        for i in range(k+1):
            ans += min(t,tickets[i])

        for i in range(k+1,len(tickets)):
            if tickets[i]>=t:
                ans+=t-1
            else:
                ans+=tickets[i]
        return ans