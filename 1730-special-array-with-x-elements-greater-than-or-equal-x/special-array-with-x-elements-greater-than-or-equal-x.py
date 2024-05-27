class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        l, r = 0, n
        nums.sort()
        while l <= r:
            mid = (l + r) // 2
            count = n - bisect.bisect_left(nums, mid)
            if count == mid:
                return mid
            elif count > mid:
                l = mid + 1
            else:
                r = mid - 1
        return -1