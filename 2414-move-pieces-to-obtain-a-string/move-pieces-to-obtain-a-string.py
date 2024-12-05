class Solution:
    def canChange(self, start: str, target: str) -> bool:
         
        x = 0
        for y in range(len(target)):
            if target[y]=="_":continue
            while x<len(start) and start[x]=="_":
                x+=1
            if x==len(start):return False
            print(x,y)
            if target[y]!=start[x]:return False
            if start[x]=="L" and x<y: return False
            if start[x]=="R" and x>y:return False
            x+=1
        
        while x<len(start) and start[x]=="_":
            x+=1
        
        return x == len(start)
