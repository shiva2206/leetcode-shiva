class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n-1
        def dfs(length,k):
            if length==1:
                return 0
            
            half = length//2 
            if k<=half:
                return dfs(half,k)
            elif k>half+1:
                return 1^dfs(half,length-k+1)
            return 1
        return str(dfs(length,k))

