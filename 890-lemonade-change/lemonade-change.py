class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr= [0,0]

        for i in bills:
            if i==5:
                arr[0]+=1
            elif i==10:
                if arr[0]==0: return False
                arr[0]-=1
                arr[1]+=1
            else:
                if arr[1]==0:
                    if arr[0]<3:return False
                    arr[0]-=3
                else:
                    arr[1]-=1
                    if arr[0]==0:return 0       
                    arr[0]-=1
        return True            