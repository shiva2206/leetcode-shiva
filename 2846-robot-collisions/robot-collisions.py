class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        l=[]
        for i in range(len(positions)):
            l.append([positions[i],healths[i],directions[i],i])
        l.sort()

        s = []
        for i in range(len(l)):
            z = True
            while s and s[-1][-2]!=l[i][-2] and l[i][-2]!='R':
                if s[-1][1] == l[i][1]:
                    s.pop()
                    z = False
                    break
                elif s[-1][1]<l[i][1]:
                    s.pop()
                    l[i][1] -=1
                else:
                    s[-1][1] -=1
                    z = False
                    break
            if z:
                s.append(l[i].copy())
        s.sort(key = lambda x : x[-1])
        res = [i[1] for i in s]
        return res
                        

