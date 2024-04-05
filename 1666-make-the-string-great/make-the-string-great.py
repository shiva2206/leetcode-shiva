class Solution:
    def makeGood(self, s: str) -> str:
        l = []

        for i in s:
            if l and (ord(l[-1])-32 == ord(i) or ord(l[-1]) + 32 == ord(i)):
                l.pop()
                continue  
            l.append(i)
        return "".join(l)

