class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        # d= {}
        # def dfs(i):
        #     if i == len(arr):return 0
        #     if i in d:return d[i]
        #     d[i] = -len(arr)
        #     req = 0
        #     s = 0
        #     for j in range(i,len(arr)):
        #         s += arr[j]
        #         req += j
        #         if req == s:
        #             d[i]  = max(d[i],1 + dfs(j+1))
        #     return d[i]
        


        # return dfs(0)

        d = [0]*(1+len(arr))
        for i in range(len(arr)-1,-1,-1):
            req = 0
            s = 0
            for j in range(i,len(arr)):
                s += arr[j]
                req += j
                if req == s:
                    d[i] = max(d[i],1 + d[j+1])
        return d[0]