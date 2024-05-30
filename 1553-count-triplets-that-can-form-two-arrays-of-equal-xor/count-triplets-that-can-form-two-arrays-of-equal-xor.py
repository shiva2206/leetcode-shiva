class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = {0:0}
        ans = 0

        p = 0
        for j in range(len(arr)):
            p ^=arr[j]
    
            if p not in d:
                d[p]=1
            ans += d[p]
        
        ans = 0
        for i in range(len(arr)):
            left = 0
            for j in range(i,len(arr)):
                left ^=arr[j]
                right = 0
                for k in range(j+1,len(arr)):
                    right^=arr[k]
                    if left == right:
                        # print(i,j,k)
                        ans+=1
        return ans