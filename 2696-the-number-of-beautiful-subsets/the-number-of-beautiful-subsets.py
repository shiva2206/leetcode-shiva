class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        d = {}
        l = {}
        s = [-abs(k)]
        def dfs(i):
            if i == len(nums):
                return 1 if len(s)>1 else 0
            q = (tuple(s),i)
            if q in d:return d[q]

            d[q] = dfs(i+1)
            if nums[i] - k not in l:
                s.append(nums[i])
                l[nums[i]] = l.get(nums[i],0) + 1
                d[q] += dfs(i+1)
                if l[nums[i]] == 1:
                    l.pop(nums[i])
                else:
                    l[nums[i]]-=1
                s.pop()
            return d[q]

        a =  dfs(0)
        # print(d)
        return a