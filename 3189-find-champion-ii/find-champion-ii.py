class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        arr = [0]*n
        ans = n
        for i,j in edges:
            arr[j]+=1
            if arr[j]==1:
                ans-=1
        if ans!=1:return -1
        for i in range(n):
            if arr[i]==0:return i
        return -1
     