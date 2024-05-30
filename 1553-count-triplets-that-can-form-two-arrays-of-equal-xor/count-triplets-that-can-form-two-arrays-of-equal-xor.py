class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = {0:[-1]}
        ans = 0
        p = 0
        for j in range(len(arr)):
            p ^=arr[j]
            if p not in d:
                d[p] = []
            for i in d[p]:
                ans += j-i-1
            d[p].append(j)
        return ans
            