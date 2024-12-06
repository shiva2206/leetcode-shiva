class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        l = set(banned)
        tot = 0
        s = 0
        for i in range(1,n+1):
            if s+i>maxSum:return tot
            if i not in l:
                s += i
                tot+=1
        return tot

