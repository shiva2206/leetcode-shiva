class Solution:
    def minSwaps(self, s: str) -> int:
        l = []
        for i in s:
            
            if l and l[-1] != i and l[-1]!=']':
                    l.pop()
                    continue
            l.append(i)
        
        return (len(l)//2 +1)//2
