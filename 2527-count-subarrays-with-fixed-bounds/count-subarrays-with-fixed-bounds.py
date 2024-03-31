class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        i = 0
        ans =0
        d=[0,0]
        a = inf
        b = -inf
        c = 0
        for j in range(len(nums)):
            if nums[j]>maxK or nums[j]<minK:
                i = j+1
                d=[0,0]
                # pq=[]
                a = inf
                b = -inf
                c = 0
                # l=[]
                continue
            if nums[j] ==minK:
                d[0]+=1
            if nums[j] == maxK:
                d[1]+=1
            a = min(a,nums[j])
            b = max(b,nums[j])   
            # d[nums[j]]+=1
            while a == minK and b==maxK:
                if nums[i]==minK:
                    d[0]-=1
                if nums[i]==maxK:
                    d[1]-=1
               
                if d[0]==0:
                    a = inf
                if d[1]==0:
                    b = -inf
                c +=1  
                i+=1

            ans += c
        return ans