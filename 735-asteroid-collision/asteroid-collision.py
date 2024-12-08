class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for i in asteroids:
            z = True
            while stack and stack[-1]>0 and i<0:
                a = stack.pop()
                b = abs(i)
                z = False
                if a == b:
                    break
                elif a>b:
                    z = False
                    stack.append(a)
                    break
                else:
                    i = -b
                    z = True
                    
            if z:
                stack.append(i)
        return stack
