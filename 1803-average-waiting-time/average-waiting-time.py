class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = 0
        t = 0

        for i,j in customers:
            if t<i:
                t = i
            t += j
            ans += t - i
        return ans/len(customers)