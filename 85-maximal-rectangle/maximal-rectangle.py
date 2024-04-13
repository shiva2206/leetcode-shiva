class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        l=[0 for i in matrix[0]]
        m=[0]
        def dfs():
            q=[]
            print(l)
            for i in range(len(l)):
                p=i
                while q and q[-1][1]>l[i]:
                    j,h=q.pop(-1)
                    p=j
                    m[0]=max(m[0],h*(i-j))
            
                q.append((p,l[i]))
            print(q)    
            for k in range(len(q)):
                j,h=q[k]
                m[0]=max(m[0],(len(l)-j)*h)
            print(m)        
        for y in range(len(matrix)):
            for z in range(len(matrix[0])):
                if matrix[y][z]=="0":
                    l[z]=0
                else:
                    l[z]+=1
            dfs()

        return m[0]                


