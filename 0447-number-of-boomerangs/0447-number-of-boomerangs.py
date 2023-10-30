class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
         ans = 0
         for x,y in points:
             d=defaultdict(int)
             for i,j in points:
                  m = math.sqrt((x-i)**2 + (y-j)**2)
                  d[m]+=1
             for k in d.values():
                 ans+=k*(k-1)
         return ans               


        