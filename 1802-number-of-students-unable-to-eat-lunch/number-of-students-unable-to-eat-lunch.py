class Solution:
    def countStudents(self, students: List[int], sand: List[int]) -> int:
        one = 0
        zer = 0
        for i in students:
            if i==1:
                one+=1
            else:
                zer+=1
        sand=sand[::-1]
        while sand:
            x = sand.pop()
            # print(x,one,zer)
            if x==0:
                if zer ==0:return one
                zer-=1
            else:
                if one==0:return zer 
                one-=1
        return 0