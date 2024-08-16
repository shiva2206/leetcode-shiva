class Solution:
    def maxDistance(self, arr: List[List[int]]) -> int:
        x = [0,1]
        if arr[0][0]>arr[1][0]:
            x[0],x[1] = x[1],x[0]
        y = [0,1]
        if arr[0][-1]>arr[1][-1]:
            y[0],y[1] = y[1],y[0]
        

        for i in range(2,len(arr)):
            if arr[i][0]<arr[x[0]][0]:
                x[0],x[1] = i,x[0]
            elif arr[i][0]<arr[x[1]][0]:
                x[1] = i
            
            if arr[i][-1]>arr[y[-1]][-1]:
                y[0],y[1] = y[1],i
            elif arr[i][-1]>arr[y[0]][-1]:
                y[0] = i
        m = 0
        for i in x:
            for j in y:
                if i!=j:
                    m = max(m,abs(arr[i][0]-arr[j][-1]))
        print(x)
        print(y)
        return m