class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        d= {}
        def dfs(i):
            if i == len(arr):return 0
            if i in d:return d[i]
            d[i] = -len(arr)
            req = 0
            s = 0
            for j in range(i,len(arr)):
                s += arr[j]
                req += j
                if req == s:
                    d[i]  = max(d[i],1 + dfs(j+1))
            return d[i]
        
        return dfs(0)
