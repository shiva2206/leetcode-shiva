class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        a = time % (n-1)
        if (time//(n-1))%2==0:
            return a +1
        return n - a