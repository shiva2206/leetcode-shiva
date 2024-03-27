class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        d=[[1]*2 for i in range(len(nums))]
        def dfs(i):
            if i in d:return d[i]
            p,q = 1,1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    x,y = dfs(j)
                    x+=1
                    if x == p:
                        q+=y
                    elif x>p:
                        p = x
                        q = y
            return [p,q]

        ans,m = 0,0

        for i in range(len(nums)-1,-1,-1):
            
            p,q = 1,1
            for j in range(len(nums)-1,i,-1):
               
           
                if nums[i]<nums[j]:
                    x,y = d[j]
                    x+=1
                    if x == p:
                        q+=y
                    elif x>p:
                        p = x
                        q = y
            d[i][0] = p
            d[i][1] = q        
            x,y = d[i]
            if ans<x:
                ans = x
                m = y
            elif x == ans:
                m+=y
        return m