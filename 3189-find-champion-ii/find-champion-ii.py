class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        arr = [0]*n
        for i,j in edges:
            arr[j]+=1
        ans = -1
        for i in range(n):
            if arr[i]==0:
                if ans==-1:
                    ans=i
                else:
                    return -1
        return ans