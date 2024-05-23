class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        l ={}
        def dfs(i):
            if i == len(nums):
                return 1 if len(l)>0 else 0
            # q = (tuple(s),i)
            # if q in d:return d[q]

            a = dfs(i+1)
            if nums[i] - k not in l :
                # s.append(nums[i])
                l[nums[i]] = l.get(nums[i],0) + 1
                a+= dfs(i+1)
                if l[nums[i]] == 1:
                    l.pop(nums[i])
                else:
                    l[nums[i]]-=1
                # s.pop()
            return a

        a =  dfs(0)
        # print(d)
        return a