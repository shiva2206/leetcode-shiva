class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
       q=abs(sx-fx)
       a=abs(sy-fy)
       if q==0 and a==0 :return t!=1
       return max(q,a)<=t



        