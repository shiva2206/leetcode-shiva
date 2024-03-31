class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        i = 0
        ans =0
        d ={}
        a = inf
        b = -inf
        c = 0
        for j in range(len(nums)):
            if nums[j]>maxK or nums[j]<minK:
                i = j+1
                d.clear()
                # pq=[]
                a = inf
                b = -inf
                c = 0
                # l=[]
                continue
            if nums[j] not in d:
                d[nums[j]] = 0
            a = min(a,nums[j])
            b = max(b,nums[j])   
            d[nums[j]]+=1
            while a == minK and b==maxK:
                d[nums[i]]-=1
                if d[nums[i]] == 0:
                    d.pop(nums[i])
                if a not in d:
                    a = inf
                if b not in d:
                    b = -inf
                c +=1  
                i+=1

            ans += c
        return ans