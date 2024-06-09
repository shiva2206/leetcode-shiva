class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d ={0:1}

        s = 0
        ans=0
        for i in range(len(nums)):
            s = (s + nums[i])%k
            ans += d.get(s,0)
            if s not in d:
                d[s] = 1
            else:
                d[s]+=1
            
            # print(i,nums[i],s,ans)
        return ans
