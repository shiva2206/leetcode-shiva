class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = bloomDay+[]
        l.sort()

        def check(t):
            c = 0
            n = 0
            for i in range(len(l)):
                if bloomDay[i]<=t:
                    n+=1
                    if n==k:
                        c+=1
                        n=0
                        if c==m:return True
                else:
                    n=0
                
        
            return False

        def binary(i,j):
            ans = -1
            while i<=j:
                m = (i+j)//2
                if check(l[m]):
                    ans = l[m]
                    j = m-1
                else:
                    i = m+1
                print(i,j)
            return ans
        return binary(0,len(l)-1)
            