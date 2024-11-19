class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        l = []
        for i in nums:
            x = 0
            y = len(l)-1
            ans= len(l)
            while x<=y:
                m = (x+y)//2
                if l[m]>=i:
                    ans = m
                    y = y-1
                else:
                    x = x +1 
            if ans == len(l):
                l.append(i)
            else:
                l[ans] = i
        print(l)
        return len(l)
