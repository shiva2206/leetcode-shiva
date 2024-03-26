class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = [nums[0]]
        for i in nums[1:]:
            if l[-1]<i:
                l.append(i)
            elif l[0]<i<l[-1]:
                l[-1] = i
            elif i<l[0]:
                l[0] = i        
            if len(l) == 3:return True
        return False        