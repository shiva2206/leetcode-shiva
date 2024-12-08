class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(i):
                    stack.pop()
                if stack and stack[-1]>0 and stack[-1] == abs(i):
                    stack.pop()
                elif not stack or stack[-1]<abs(i):

                    stack.append(i)
                    
        return stack
