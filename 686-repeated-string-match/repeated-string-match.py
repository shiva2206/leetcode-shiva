class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        q = ceil(len(b)/len(a))
        p = a*q
        if b in p:return q
        if b in p+a:return q+1
        return -1