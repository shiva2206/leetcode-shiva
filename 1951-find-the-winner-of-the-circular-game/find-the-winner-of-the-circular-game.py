class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        l = [True]*(n+1)
        
        x=1
        for i in range(n-1):
            
            y= 0
            while True:
                if x == n+1:
                    x = 1
                if l[x]:
                    y+=1
                    if y == k:
                        
                        l[x]=False
                        x+=1
                        break
                x+=1
        
        for q in range(1,len(l)):
            if l[q]:return q
        return -1
