class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        ans = 0
        
        
        m = 0
        t = 0
        i = 0
        for j in range(len(customers)):
            if grumpy[j]==1:
                t+=customers[j]
            else:
                ans+= customers[j]
            if j - i ==minutes:
                if grumpy[i]==1:
                    t -=customers[i]
                i+=1
            m = max(m,t)
        print(m)
        return ans+m
